import { createSidebar } from "../components/sidebar.js";
import { createHeader } from "../components/header.js";
import { createDashboard } from "../components/dashboard.js";

const app = document.getElementById("app");

app.innerHTML = `
<div class="app">

    ${createSidebar()}

    <main class="content">

        ${createHeader("Dashboard")}

        ${createDashboard()}

    </main>

</div>
`;
