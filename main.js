function openCity(evt, cityName) {
    var i, x, tablinks;

    // Hide all city divs
    x = document.getElementsByClassName("city");
    for (i = 0; i < x.length; i++) {
        x[i].style.display = "none";
    }

    // Remove the active-tab class from all tab buttons
    tablinks = document.getElementsByClassName("tablink");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].classList.remove("active-tab");
    }

    // Show the selected city div
    document.getElementById(cityName).style.display = "block";

    // Add the active-tab class to the clicked tab button
    evt.currentTarget.classList.add("active-tab");

    // Handle image changes dynamically for a single image
    const dynamicImage = document.getElementById("dynamicImage");
    if (cityName === "LoremIpsum") {
        dynamicImage.setAttribute('src', 'book_3_24dp_E3E3E3_FILL1_wght400_GRAD0_opsz24.png');
    } else if (cityName === "DolorSitAmet") {
        dynamicImage.setAttribute('src', 'videocam_24dp_E3E3E3_FILL1_wght400_GRAD0_opsz24.png');
    }
}