document.addEventListener("DOMContentLoaded", function() {
    const toggleButton = document.getElementById("toggle-posts");
    const postsContainer = document.getElementById("posts-container");

    toggleButton.addEventListener("click", function() {
        if (postsContainer.style.display === "none" || postsContainer.style.display === "") {
            postsContainer.style.display = "block";
            toggleButton.textContent = "Hide Posts";
        } else {
            postsContainer.style.display = "none";
            toggleButton.textContent = "View Posts";
        }
    });
});