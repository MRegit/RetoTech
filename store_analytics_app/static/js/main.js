const getOptionChart = async () => {
    try {
        const response = await fetch("http://127.0.0.1:8000/get_chart/");
        return await response.json();
    } catch (ex) {
        alert(ex);
    }
};

const initChart = async () => {
    const myChart = echarts.init(document.getElementById("chartPrueba"));

    myChart.setOption(await getOptionChart());

    myChart.resize();
};

const getDemandTrends = async () => {
    try {
        const response = await fetch("http://127.0.0.1:8000/demand_trends_chart/");
        return await response.json();
    } catch (ex) {
        alert(ex);
    }
};

const initChartDemandTrends= async () => {
    const myChart = echarts.init(document.getElementById("chartDemandTrends"));
    myChart.on('updateAxisPointer', function (event) {
        const xAxisInfo = event.axesInfo[0];
        if (xAxisInfo) {
          const dimension = xAxisInfo.value + 1;
          myChart.setOption({
            series: {
              id: 'pie',
              label: {
                formatter: '{b}: {@[' + dimension + ']} ({d}%)'
              },
              encode: {
                value: dimension,
                tooltip: dimension
              }
            }
          });
        }
      });

    myChart.setOption(await getDemandTrends());

    myChart.resize();
};

const getMapStore = async () => {
    try {
        const response = await fetch("http://127.0.0.1:8000/mapStore/");
        return await response.json();
    } catch (ex) {
        alert(ex);
    }
};

const initChartMapStore = async () => {
    const myChart = echarts.init(document.getElementById("chartMapStore"));

    myChart.setOption(await getMapStore());
    myChart.resize();
};

const getBarDemand = async () => {
    try {
        const response = await fetch("http://127.0.0.1:8000/chartBarDemand/");
        return await response.json();
    } catch (ex) {
        alert(ex);
    }
};

const initChartBarDemand= async () => {
    const myChart = echarts.init(document.getElementById("chartBarDemand"));

    myChart.setOption(await getBarDemand());

    myChart.resize();
};

window.addEventListener("load", async () => {

    await initChartDemandTrends();

});

window.addEventListener("load", async () => {

    await initChartMapStore();

});

window.addEventListener("load", async () => {

    await initChartBarDemand();
});
