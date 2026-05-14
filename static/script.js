function showToast(message) {
    const toast = document.getElementById("toast");
    toast.textContent = message;
    toast.classList.add("show");

    setTimeout(() => {
        toast.classList.remove("show");
    }, 2000);
}

function copyCode() {
    const codeElement = document.getElementById("generatedCode");

    if (!codeElement) {
        showToast("No code found!");
        return;
    }

    navigator.clipboard.writeText(codeElement.textContent)
        .then(() => showToast("Code copied!"))
        .catch(() => showToast("Copy failed"));
}

document.addEventListener("DOMContentLoaded", () => {
    if (window.Prism) {
        requestAnimationFrame(() => Prism.highlightAll());
    }
});