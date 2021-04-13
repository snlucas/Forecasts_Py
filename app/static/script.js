function collapse() {
    let collapseWeekForecast = document.querySelector("ul.week-forecasts");

    console.log("oi");
    if(collapseWeekForecast.style.display == "none") {
        collapseWeekForecast.style.display = "block";
        collapseWeekForecast.style.overflow = "visible";
    } else {
        collapseWeekForecast.style.display = "none";
        collapseWeekForecast.style.overflow = "hidden";
    }
}
