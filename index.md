---
layout: default
---

# 👋 Hi, I'm Zwi (Duy DO)

A developer building real-world applications with **Java**, **C# (.NET Framework)** and **Python**.
Currently taking the IBM Full-Stack course — microservices, GenAI integration and full JavaScript projects.

## 🚀 Featured Projects

- **[BilliardsTournament](https://github.com/dophucduy/BilliardsTournament)** — web app for organizing billiards tournaments, tracking and results. _Java, Tomcat, HTML/CSS/JS_
- **[DrugPrevention](https://github.com/dophucduy/DrugPrevention)** — RESTful API for counterfeit drug prevention, product verification and traceability. _C#, .NET_

## 🆕 Latest Repositories

<ul id="repos"><li>Loading… (or see <a href="https://github.com/{{ site.github_username }}?tab=repositories">all repositories</a>)</li></ul>

<script>
fetch("https://api.github.com/users/{{ site.github_username }}/repos?per_page=100&sort=pushed")
  .then(r => r.json())
  .then(list => {
    const esc = s => String(s).replace(/[&<>"]/g, c => ({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]));
    const repos = list.filter(r => !r.fork && !r.archived && r.name.toLowerCase() !== "{{ site.github_username }}").slice(0, 6);
    document.getElementById("repos").innerHTML = repos.map(r =>
      `<li><a href="${r.html_url}"><strong>${esc(r.name)}</strong></a>` +
      (r.description ? ` — ${esc(r.description)}` : "") +
      (r.language ? ` · <code>${esc(r.language)}</code>` : "") + `</li>`).join("");
  })
  .catch(() => {});
</script>

## 🛠️ Tech Stack

<p class="stack">
{% assign icons = "java/java-original,tomcat/tomcat-original,csharp/csharp-original,dot-net/dot-net-original,python/python-original,html5/html5-original,css3/css3-original,javascript/javascript-original,git/git-original,github/github-original" | split: "," %}
{% for i in icons %}<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/{{ i }}.svg" alt="{{ i | split: '/' | first }}">{% endfor %}
</p>

## 📫 Contact

- Email: [doychannel1802@gmail.com](mailto:doychannel1802@gmail.com)
- LinkedIn: [Duy DO](https://www.linkedin.com/in/doychannel1802/)
- GitHub: [dophucduy](https://github.com/dophucduy)

