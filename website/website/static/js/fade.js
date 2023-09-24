<script>
    // Your existing code for sign-up and sign-in buttons

    const messages = document.querySelectorAll('.message');

    function fadeOutMessages() {
        messages.forEach((message) => {
            setTimeout(() => {
                message.style.opacity = '0';
            }, 5000); // 5000 milliseconds (5 seconds) delay before fading out
        });
    }

    // Call the fadeOutMessages function when the page loads
    window.addEventListener('load', fadeOutMessages);
</script>