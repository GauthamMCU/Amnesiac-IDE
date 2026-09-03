async function runAndVanish() {
    if (!window.editor) {
        console.warn("Editor is still loading, please wait...");
        return;
    }

    const code = window.editor.getValue();
    const outputConsole = document.getElementById("output");

    if (!code.trim()) return;

    // Clear code instantly
    window.editor.setValue("");

    try {
        const response = await fetch("/execute", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ code: code })
        });
        const data = await response.json();
        outputConsole.innerText = data.output;
    } catch (err) {
        outputConsole.innerText = "[ERROR] " + err.message;
    }
}