# Weather Station

This project is for developing a weather station with Flask, a python framwork. It uses Open Weather API to get the weather data.

## Acknowledgements

- [Open Weather API](https://openweathermap.org/api)

## API Reference

#### Get Weather Data

```http
  GET /api/${city_name}&appid=${app_id}
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `app_id`  | `string` | **Required**. Your API key |

#### Parameter

| Parameter    | Type  | Description            |
| :----------- | :---- | :--------------------- |
| `temp`       | `int` | Main Temperture        |
| `feels_like` | `int` | Feels Like Temperature |
| `temp_min`   | `int` | Minimum Temperature    |
| `temp_max`   | `int` | Maximum Temperature    |
| `humidity`   | `int` | Humidity               |
| `pressure`   | `int` | Pressure               |
| `speed`      | `int` | Wind Speed             |

## Screenshots

#### Home Screen

![home-page](https://github.com/Jyoti-Chakma/Weather-Station-with-Flask/blob/master/Screenshots/home.png)

#### Home Screen

![Weather Result 1](https://github.com/Jyoti-Chakma/Weather-Station-with-Flask/blob/master/Screenshots/result1.png)

#### Home Screen

![Weather Result 2](https://github.com/Jyoti-Chakma/Weather-Station-with-Flask/blob/master/Screenshots/result2.png)

## License

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://github.com/Jyoti-Chakma/Weather-Station-with-Flask/blob/master/LICENSE.txt)

## Contributing

Contributions are always welcome!
