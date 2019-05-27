$(function(){
    $.post('/home/',{'start':1},function (data) {

    })
});


var popCanvas = document.getElementById("popChart").getContext("2d");
    var barChart = new Chart(popCanvas, {
        type: 'doughnut',
        data: {
            labels: ["好", "中等", "差"],
            datasets: [{
                label: 'Population',
                data: [90, 20, 40],
                backgroundColor: [
                    'rgba(255, 99, 132, 0.6)',
                    'rgba(54, 162, 235, 0.6)',
                    'rgba(255, 206, 86, 0.6)',
                    // 'rgba(75, 192, 192, 0.6)',
                    // 'rgba(153, 102, 255, 0.6)',
                    // 'rgba(255, 159, 64, 0.6)',
                    // 'rgba(255, 99, 132, 0.6)',
                    // 'rgba(54, 162, 235, 0.6)',
                    // 'rgba(255, 206, 86, 0.6)',
                    // 'rgba(75, 192, 192, 0.6)',
                    // 'rgba(153, 102, 255, 0.6)'
                ]
            }]
        }
    });