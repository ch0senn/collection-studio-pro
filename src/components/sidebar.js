"use strict";

export function createSidebar(active = "dashboard") {
    const items = [
        { id: "dashboard", label: "Dashboard" },
        { id: "collections", label: "Collections" },
        { id: "assets", label: "Assets" },
        { id: "import", label: "Import" },
        { id: "export", label: "Export" },
        { id: "settings", label: "Settings" }
    ];

    return `
        <aside class="sidebar">

            <div class="logo">
                <span class="logo-icon">◆</span>

                <div>
                    <h1>Collection Studio</h1>
                    <small>Professional Edition</small>
                </div>

            </div>

            <nav class="navigation">

                ${items.map(item => `
                    <button
                        class="nav-button ${item.id === active ? "active" : ""}"
                        data-page="${item.id}">
                        ${item.label}
                    </button>
                `).join("")}

            </nav>

        </aside>
    `;
}
