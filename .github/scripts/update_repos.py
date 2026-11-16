"""Rewrite the block between REPOS:START / REPOS:END in README.md with the latest public repos."""
import json, os, re, urllib.request

USER = os.environ.get("GH_USER", "dophucduy")
LIMIT = int(os.environ.get("REPO_LIMIT", "6"))

req = urllib.request.Request(
    f"https://api.github.com/users/{USER}/repos?per_page=100&sort=pushed",
    headers={"Accept": "application/vnd.github+json",
             **({"Authorization": f"Bearer {os.environ['GITHUB_TOKEN']}"} if os.environ.get("GITHUB_TOKEN") else {})},
)
repos = json.load(urllib.request.urlopen(req))
repos = [r for r in repos if not r["fork"] and not r["archived"] and r["name"].lower() != USER.lower()][:LIMIT]

lines = []
for r in repos:
    desc = f" — {r['description']}" if r["description"] else ""
    lang = f" · `{r['language']}`" if r["language"] else ""
    lines.append(f"- [{r['name']}]({r['html_url']}){desc}{lang}")

with open("README.md", encoding="utf-8") as f:
    readme = f.read()
new = re.sub(r"(<!-- REPOS:START -->).*?(<!-- REPOS:END -->)",
             lambda m: m.group(1) + "\n" + "\n".join(lines) + "\n" + m.group(2), readme, flags=re.S)
with open("README.md", "w", encoding="utf-8", newline="") as f:
    f.write(new)
print("\n".join(lines))

