const savedData =
  sessionStorage.getItem("comparisonData")

if (!savedData) {

  document.body.innerHTML = `
    <div style="
      min-height: 100vh;
      display: flex;
      align-items: center;
      justify-content: center;
      background: #f9f8f5;
      color: #1a1a1a;
      font-family: Inter, sans-serif;
      letter-spacing: 0.05em;
    ">
      no comparison data found
    </div>
  `

  throw new Error("No session data")

}

const data = JSON.parse(savedData)

const profile1 = data.user1
const profile2 = data.user2

// TOP SCORE AREA
document.getElementById("user1-name").textContent =
  profile1.profile.login

document.getElementById("user2-name").textContent =
  profile2.profile.login

// GITHUB LINKS
document.getElementById("user1-name").href =
  profile1.profile.html_url

document.getElementById("user2-name").href =
  profile2.profile.html_url

// SCORES
document.getElementById("user1-score").textContent =
  profile1.codex_score.toFixed(2)

document.getElementById("user2-score").textContent =
  profile2.codex_score.toFixed(2)

// WINNER
document.getElementById("winner-text").textContent =
  `${data.winner.toUpperCase()} WON.`

// CARDS
fillCard(profile1, 1)
fillCard(profile2, 2)

// WINNER BORDER
if (
  data.winner.toLowerCase() ===
  profile1.profile.login.toLowerCase()
) {

  document.getElementById("card1")
    .classList.add("card--winner")

} else {

  document.getElementById("card2")
    .classList.add("card--winner")

}

function fillCard(userData, number) {

  const profile = userData.profile
  const stats = userData.stats

  // TOP LANGUAGE
  let topLanguage = "Unknown"

  if (Object.keys(stats.languages).length > 0) {

    topLanguage = Object.keys(stats.languages)
      .reduce((a, b) =>
        stats.languages[a] > stats.languages[b] ? a : b
      )

  }

  // AVATAR
  document.getElementById(`avatar${number}`).src =
    profile.avatar_url

  // USERNAME
  document.getElementById(`card${number}-username`).textContent =
    profile.login

  // TITLE
  document.getElementById(`card${number}-title`).textContent =
    `${profile.public_repos} repos · ${topLanguage}`

  // SUMMARY
  document.getElementById(`summary${number}`).textContent =
    userData.summary

  // STATS
  document.getElementById(`stars${number}`).textContent =
    stats.total_stars.toLocaleString()

  document.getElementById(`forks${number}`).textContent =
    stats.total_forks.toLocaleString()

  document.getElementById(`followers${number}`).textContent =
    profile.followers.toLocaleString()

  document.getElementById(`repos${number}`).textContent =
    profile.public_repos

  // LANGUAGES
  document.getElementById(`languages${number}`).textContent =
    Object.keys(stats.languages).join(", ")

  // BADGES
  const badgesContainer =
    document.getElementById(`badges${number}`)

  badgesContainer.innerHTML = ""

  userData.badges.forEach(badge => {

    const badgeElement = document.createElement("span")

    badgeElement.classList.add("badge")

    badgeElement.textContent = badge

    badgesContainer.appendChild(badgeElement)

  })

}