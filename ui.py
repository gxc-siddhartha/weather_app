import flet as ft
import aiohttp

from datetime import *

weatherInfo = {}

location = "/Users/siddhartha/Developer/weather_app/images/"

oneCallData = {}

oneCallData['city'] = ""
oneCallData['temp'] = ""
oneCallData['pressure'] = ""
oneCallData['humidity'] = ""
oneCallData['dew_point'] = ""
oneCallData['uvi'] = ""
oneCallData['wind_speed'] = ""
oneCallData['sunrise'] = ""
oneCallData['sunset'] = ""
oneCallData['time'] = ""
oneCallData['main'] = ""
oneCallData['icon'] = ""
oneCallData['daily'] = [{}]
oneCallData['visibility'] = ""


API_KEY = 'your api key'

teal = "#135d66"
teal10 = "#17717c"
teal20 = "#1b8693"
teal30 = "#a1bec2"
teal10x = "#0f484f"
teal_faded = "#d0dfe0"

white = "#ffffff"
white_grey = "#ECECEC"

c_p_row = ft.Row(
    alignment=ft.MainAxisAlignment.SPACE_EVENLY,
    vertical_alignment=ft.CrossAxisAlignment.CENTER,
    width=820,
    controls=[],
)

c_p_widget_title = ft.Text(
                        value="visibility",
                        style=ft.TextStyle(
                                font_family="IBM Plex Mono",
                                size=18,
                                weight=ft.FontWeight.BOLD,
                                color="#B2B2B2"
                            ),
                        )

cp_widget_image = ft.Image(
                            src=f"{location}vis.png",
                            height=50,
                            width=50,
                            fit=ft.ImageFit.FIT_HEIGHT,
                        )

cp_widget_content =  ft.Text(
                value="100",
                style=ft.TextStyle(
                    font_family="Azeret Mono",
                    size=76,
                    letter_spacing=-6,
                ),
                spans=[
                    ft.TextSpan(
                        text=" km",
                        style=ft.TextStyle(
                            font_family="Azeret Mono",
                            size=24, 
                            color="#B2B2B2",
                            letter_spacing=-6,
                            weight=ft.FontWeight.BOLD
                        )
                    ),
                ]
            )

c_p_widget = ft.Container(
    width=264, 
    height=182,
    padding=ft.padding.only(top=20, left=20, right=20, bottom=3),
    bgcolor=ft.colors.WHITE,
    border_radius=ft.border_radius.all(30),
    margin=ft.margin.only(bottom=10, right=10, left=10, top=0),
    content=ft.Column(
        controls=[
                ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    vertical_alignment=ft.CrossAxisAlignment.START,
                    controls=[
                        c_p_widget_title,
                        cp_widget_image,

                    ]
                ),
                
        
            ft.Text(
                value="100",
                style=ft.TextStyle(
                    font_family="Azeret Mono",
                    size=76,
                    letter_spacing=-6,
                ),
                spans=[
                    ft.TextSpan(
                        text=" km",
                        style=ft.TextStyle(
                            font_family="Azeret Mono",
                            size=24, 
                            color="#B2B2B2",
                            letter_spacing=-6,
                            weight=ft.FontWeight.BOLD
                        )
                    ),
                ]
            )
        ]
    )
)
c_p_widget2 = ft.Container(
    width=264, 
    height=182,
    padding=ft.padding.only(top=20, left=20, right=20, bottom=3),
    bgcolor=ft.colors.WHITE,
    border_radius=ft.border_radius.all(30),
    margin=ft.margin.only(bottom=10, right=10, left=10, top=0),
    content=ft.Column(
        controls=[
            c_p_widget_title,
            ft.Text(
                value="100",
                style=ft.TextStyle(
                    font_family="Azeret Mono",
                    size=76,
                    letter_spacing=-6,
                ),
                spans=[
                    ft.TextSpan(
                        text=" km",
                        style=ft.TextStyle(
                            font_family="Azeret Mono",
                            size=24, 
                            color="#B2B2B2",
                            letter_spacing=-6,
                            weight=ft.FontWeight.BOLD
                        )
                    ),
                ]
            )
        ]
    )
)
    

d_a_day = ft.Text(
                value="Sun",
                style=ft.TextStyle(
                    size=16,
                    font_family="IBM Plex Sans",
                    weight=ft.FontWeight.BOLD,
                    
                ),
            )


progress_ring = ft.Container(
            height=680, 
            width=1200, 
            alignment=ft.alignment.center,
            content=ft.Column(
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.ProgressRing(color=ft.cupertino_colors.BLACK)
                ]
            )
        )
    
error_frame = ft.Container(
            height=680, 
            width=1200, 
            alignment=ft.alignment.center,
            content=ft.Column(
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Image(
                        src=f"{location}error.png",
                        height=60,
                        width=60,
                        fit=ft.ImageFit.FIT_HEIGHT
                    ),
                    ft.Container(
                        height=5    
                    ),
                    ft.Text(
                        value = "Check your spelling!",
                        style = ft.TextStyle(
                            font_family="SF Pro Display",
                            size=18,
                            color="#A7A7A7"
                        )
                    ),
                ]
            )
        )

def main(page: ft.Page):
    page.window_resizable = False
    page.window_height = 800
    page.window_width = 1200
    
    # page.platform_brightness=ft.Brightness.LIGHT
    page.theme=ft.Theme(
        color_scheme_seed= teal,
        use_material3=False,
        font_family="SF Pro Text"
       
    )
    page.padding = 0
    page.bgcolor = ft.colors.WHITE
    
    async def fetch_weather_data(city):
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                data = await response.json()
                return data

    async def getOneCallData(lat, lon):
        url = f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&units=metric&appid=ef7de04474aa0848c9a9f48a2b3d2811"
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                data = await response.json()
                return data
            
    daily_analysis_row = ft.Row(
                scroll=ft.ScrollMode.HIDDEN,
            ) 
    
    temo_dc = ft.Container(
                    height=121,
                    margin=ft.margin.only(left=10, right=0, top=20, bottom=20),
                    border_radius=ft.border_radius.all(20),
                    width=111, 
                    border=ft.border.all(width=1, color="#9F9F9F"),
                    content=ft.Column(
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            ft.Text(
                                # value=f"{daily_formatted_day}",
                                value=f"Mon",
                                style=ft.TextStyle(
                                    size=16,
                                    font_family="IBM Plex Sans",
                                    weight=ft.FontWeight.BOLD,
                                    
                                ),
                            ),
                            ft.Image(
                                src=f"{location}01d.png",
                                height=35, 
                                width=35, 
                                fit=ft.ImageFit.FIT_HEIGHT,
                            ),
                            ft.Row(
                                alignment=ft.MainAxisAlignment.CENTER,
                                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                controls=[
                                    ft.Text(
                                        value=f"36°C",
                                        style=ft.TextStyle(
                                            font_family="IBM Plex Mono",
                                            size="14",
                                            weight=ft.FontWeight.BOLD
                                        ),
                                    ),
                                    ft.Text(
                                        value=f"29°C",
                                        style=ft.TextStyle(
                                            font_family="IBM Plex Mono",
                                            size="14",
                                            color="#A7A7A7",
                                            weight=ft.FontWeight.BOLD
                                        ),
                                    ),
                                ]
                            ),
                        ]
                    )
                )
    
    for i in range(0, 8):
        daily_analysis_row.controls.append(temo_dc)  
     
    async def apimain(e):
        page.clean()
        page.add(progress_ring)
        page.update()
        
        try:
            weather_data = await fetch_weather_data(str(location_textfield.value))
            
            weatherInfo['lat'] =  weather_data['coord']['lat']
            weatherInfo['lon'] =  weather_data['coord']['lon']
            
            lat = weatherInfo['lat']
            lon = weatherInfo['lon']
            
            oCData = await getOneCallData(lat, lon)
            
            oneCallData['temp'] = oCData['current']['temp']
            oneCallData['pressure'] = oCData['current']['pressure']
            oneCallData['humidity'] = oCData['current']['humidity']
            oneCallData['dew_point'] = oCData['current']['dew_point']
            oneCallData['uvi'] = oCData['current']['uvi']
            oneCallData['wind_speed'] = oCData['current']['wind_speed']
            oneCallData['sunrise'] = oCData['current']['sunrise']
            oneCallData['sunset'] = oCData['current']['sunset']
            oneCallData['time'] = oCData['current']['dt']
            oneCallData['main'] = oCData['current']['weather'][0]['main']
            oneCallData['icon'] = oCData['current']['weather'][0]['icon']
            oneCallData['daily'] = oCData['daily']
            oneCallData['visibility'] = oCData['current']['visibility']
            print(oneCallData['icon'])
            
            page.clean()
            page.add(weather_frame)
            page.update()
        except:
            page.clean()
            page.add(error_frame)
            page.update()
            
    async def apimain_t(e):
        page.clean()
        page.add(progress_ring)
        page.update()
        
        try:
            weather_data = await fetch_weather_data(str(location_textfield.value))
            
            weatherInfo['lat'] =  weather_data['coord']['lat']
            weatherInfo['lon'] =  weather_data['coord']['lon']
            
            lat = weatherInfo['lat']
            lon = weatherInfo['lon']
            
            oCData = await getOneCallData(lat, lon)
            
            oneCallData['city'] = str(location_textfield.value)
            oneCallData['temp'] = oCData['current']['temp']
            oneCallData['pressure'] = oCData['current']['pressure']
            oneCallData['humidity'] = oCData['current']['humidity']
            oneCallData['dew_point'] = oCData['current']['dew_point']
            oneCallData['uvi'] = oCData['current']['uvi']
            oneCallData['wind_speed'] = oCData['current']['wind_speed']
            oneCallData['sunrise'] = oCData['current']['sunrise']
            oneCallData['sunset'] = oCData['current']['sunset']
            oneCallData['time'] = oCData['current']['dt']
            oneCallData['main'] = oCData['current']['weather'][0]['main']
            oneCallData['icon'] = oCData['current']['weather'][0]['icon']
            oneCallData['daily'] = oCData['daily']
            oneCallData['visibility'] = round((oCData['current']['visibility'])/1000)
            

            sunset_t = datetime.fromtimestamp(oneCallData['sunset']).strftime('%-I:%M %p')
            sunrise_t = datetime.fromtimestamp(oneCallData['sunrise']).strftime('%-I:%M %p')

            print(oneCallData['icon'])
        
            daily_tile = oneCallData['daily']
            
            for i in range(0, len(daily_tile)):
                day = datetime.fromtimestamp(daily_tile[i]['dt']).strftime('%a')
                max = daily_tile[i]['temp']['max']
                min = daily_tile[i]['temp']['min']
                icon = daily_tile[i]['weather'][0]['icon']
                
                print(day)
                print(min)
                print(max)
                print(icon)
                
                
                
                daily_analysis_container = ft.Container(
                    height=121,
                    margin=ft.margin.only(left=10, right=0, top=20, bottom=20),
                    border_radius=ft.border_radius.all(20),
                    width=111, 
                    border=ft.border.all(width=1, color="#9F9F9F"),
                    content=ft.Column(
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            ft.Text(
                                # value=f"{daily_formatted_day}",
                                value=f"{day}",
                                style=ft.TextStyle(
                                    size=16,
                                    font_family="IBM Plex Sans",
                                    weight=ft.FontWeight.BOLD,
                                    
                                ),
                            ),
                            ft.Image(
                                src=f"{location}{icon}.png",
                                height=35, 
                                width=35, 
                                fit=ft.ImageFit.FIT_HEIGHT,
                            ),
                            ft.Row(
                                alignment=ft.MainAxisAlignment.CENTER,
                                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                controls=[
                                    ft.Text(
                                        value=f"{round(max)}°C",
                                        style=ft.TextStyle(
                                            font_family="IBM Plex Mono",
                                            size="14",
                                            weight=ft.FontWeight.BOLD
                                        ),
                                    ),
                                    ft.Text(
                                        value=f"{round(min)}°C",
                                        style=ft.TextStyle(
                                            font_family="IBM Plex Mono",
                                            size="14",
                                            color="#A7A7A7",
                                            weight=ft.FontWeight.BOLD
                                        ),
                                    ),
                                ]
                            ),
                        ]
                    )
                )
                daily_analysis_row.controls[i] = daily_analysis_container
                
            
            formatted_day = datetime.fromtimestamp(oneCallData['time']).strftime('%A')
            formatted_date = datetime.fromtimestamp(oneCallData['time']).strftime('%-d %B')
            
            if 'd' in str(oneCallData['icon']):
                oneCallData['day_phase'] = "day"
            else:
                oneCallData['day_phase'] = "night"
            
            weather_frame = ft.Container(
                animate=ft.animation.Animation(1000, ft.AnimationCurve.EASE_IN_OUT),
                opacity=50,
                bgcolor="#F7F7F7",
                content=ft.Row(
                    alignment=ft.MainAxisAlignment.START,
                    vertical_alignment=ft.CrossAxisAlignment.START,
                    controls=[
                        ft.Container(
                            width=294,
                            padding=ft.padding.all(20),
                            height=page.window_height,
                            bgcolor=ft.colors.WHITE,
                            shadow=ft.BoxShadow(
                                            spread_radius=-80,
                                            blur_radius=50,
                                            color="#b3b3b3"
                                        ),
                            content=ft.Column(
                                controls=[
                                    ft.Text(
                                        text_align=ft.TextAlign.START,
                                        value =f"{oneCallData['city']}",
                                        style=ft.TextStyle(
                                            weight=ft.FontWeight.W_700,
                                            size=36,
                                            letter_spacing=-2,
                                        )
                                    ),
                                    ft.Container(
                                        height=5,
                                    ),
                                    ft.Image(
                                        src=f"{location}{oneCallData['icon']}.png",
                                        width=264, 
                                        height=210,
                                        fit=ft.ImageFit.CONTAIN
                                    ),
                                    ft.Container(
                                        height=10    
                                    ),
                                    ft.Text(
                                        value=f"{round(oneCallData['temp'])}°C",
                                        style=ft.TextStyle(
                                            font_family="IBM Plex Mono",
                                            size=64, 
                                            letter_spacing=-5,
                                            weight=ft.FontWeight.BOLD,
                                            height=0.8,
                                        )
                                    ),
                                    ft.Text(
                                    value = f"{formatted_day}",
                                        style=ft.TextStyle(
                                            font_family="IBM Plex Mono",
                                            size=24,
                                            letter_spacing=-1,
                                            weight=ft.FontWeight.BOLD,
                                        ),
                                        spans=[
                                                ft.TextSpan(
                                                    text = f", {formatted_date}",
                                                    style=ft.TextStyle(
                                                        font_family="IBM Plex Mono", 
                                                        size=24,
                                                        letter_spacing=-1,
                                                        weight=ft.FontWeight.NORMAL
                                                    )
                                                )
                                            ],
                                    ),
                                    ft.Divider(
                                        height=20,
                                        color="#6B6B6B" 
                                    ),
                                    ft.Text(
                                        value=f"{oneCallData['main']}",
                                        style=ft.TextStyle(
                                            size=18,
                                            weight=ft.FontWeight.BOLD,
                                            letter_spacing=-1,
                                        ),
                                    ),
                                    ft.Row(
                                        alignment=ft.MainAxisAlignment.START,
                                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                        controls=[
                                            ft.Image(
                                                src=f"{location}gauge.png",
                                                height=22,
                                                width=22,
                                                fit=ft.ImageFit.FIT_HEIGHT,
                                            ),
                                            ft.Text(
                                                "Pressure:",
                                                style=ft.TextStyle(
                                                    font_family="IBM Plex Mono",
                                                    size=18,
                                                    letter_spacing=-1,
                                                    height=0.8,
                                                    weight=ft.FontWeight.BOLD
                                                ),
                                                spans=[
                                                    ft.TextSpan(
                                                        text = f" {oneCallData['pressure']}kPa",
                                                        style=ft.TextStyle(
                                                            font_family="Azeret Mono",
                                                            size=18,
                                                            weight=ft.FontWeight.NORMAL
                                                        ),
                                                    )
                                                ]
                                            ),
                                        ],
                                    ),
                                    ft.Container(
                                        height=0,    
                                    ),
                                    ft.Container(
                                        height=160,
                                        width=254,
                                        border_radius=ft.border_radius.all(20),
                                        bgcolor="#F6F6F6",
                                        content=ft.Image(
                                            
                                            src= f"{location}{oneCallData['day_phase']}.jpeg",
                                            fit=ft.ImageFit.FIT_HEIGHT
                                        ),
                                    )
                                ]
                            ),
                        ),
                        ft.Container(
                            height=page.window_height,
                            bgcolor="#F7F7F7",
                            padding=ft.padding.all(20),
                            alignment=ft.alignment.top_center,
                            
                            content=ft.Column(
                                alignment=ft.MainAxisAlignment.START,
                                controls=[
                                    
                                    ft.Text(
                                        "Daily",
                                        style=ft.TextStyle(
                                            font_family="IBM Plex Mono",
                                            size=24,
                                            weight=ft.FontWeight.BOLD,
                                            letter_spacing=-1,
                                            
                                        ),
                                        spans=[
                                            ft.TextSpan(
                                                text=" Analysis",
                                                style=ft.TextStyle(
                                                    font_family="IBM Plex Mono",
                                                    size=24,
                                                    weight=ft.FontWeight.NORMAL,
                                                    letter_spacing=-1,
                                                ),
                                            )
                                        ]
                                    ),
                                    ft.Container(
                                        border_radius=ft.border_radius.all(20),
                                        height=161,
                                        padding=ft.padding.symmetric(vertical=0, horizontal=10),
                                        shadow=ft.BoxShadow(
                                            spread_radius=-50,
                                            blur_radius=100,
                                            color="#b3b3b3"
                                        ),
                                        width=845,
                                        bgcolor=ft.colors.WHITE,
                                        content=daily_analysis_row,
                                    ),
                                    ft.Container(
                                        height=10,
                                    ),
                                    ft.Text(
                                        "Current",
                                        style=ft.TextStyle(
                                            font_family="IBM Plex Mono",
                                            size=24,
                                            weight=ft.FontWeight.BOLD,
                                            letter_spacing=-1,
                                            
                                        ),
                                        spans=[
                                            ft.TextSpan(
                                                text=" Parameters",
                                                style=ft.TextStyle(
                                                    font_family="IBM Plex Mono",
                                                    size=24,
                                                    weight=ft.FontWeight.NORMAL,
                                                    letter_spacing=-1,
                                                ),
                                            )
                                        ]
                                    ),
                                    ft.Column(
                                        alignment=ft.MainAxisAlignment.CENTER,
                                        horizontal_alignment=ft.CrossAxisAlignment.START,
                                        controls=[
                                            ft.Row(
                                                alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                                                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                                width=820,
                                                controls=[
                                                    
                                                    ft.Container(
                                                        width=264, 
                                                        height=182,
                                                        padding=ft.padding.only(top=20, left=20, right=20, bottom=3),
                                                        bgcolor=ft.colors.WHITE,
                                                        border_radius=ft.border_radius.all(30),
                                                        margin=ft.margin.only(bottom=10, right=10, left=10, top=0),
                                                        content=ft.Column(
                                                            controls=[
                                                                    ft.Row(
                                                                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                                                        vertical_alignment=ft.CrossAxisAlignment.START,
                                                                        controls=[
                                                                            ft.Text(
                                                                            value="visibility",
                                                                            style=ft.TextStyle(
                                                                                    font_family="IBM Plex Mono",
                                                                                    size=18,
                                                                                    weight=ft.FontWeight.BOLD,
                                                                                    color="#B2B2B2"
                                                                                ),
                                                                            ),
                                                                            ft.Image(
                                                                                src=f"{location}vis.png",
                                                                                height=50,
                                                                                width=50,
                                                                                fit=ft.ImageFit.FIT_HEIGHT,
                                                                            ),

                                                                        ]
                                                                    ),
                                                                    
                                                            
                                                                ft.Text(
                                                                    value=f"{oneCallData['visibility']}",
                                                                    style=ft.TextStyle(
                                                                        font_family="Azeret Mono",
                                                                        size=76,
                                                                        letter_spacing=-6,
                                                                    ),
                                                                    spans=[
                                                                        ft.TextSpan(
                                                                            text=" km",
                                                                            style=ft.TextStyle(
                                                                                font_family="Azeret Mono",
                                                                                size=24, 
                                                                                color="#B2B2B2",
                                                                                letter_spacing=-6,
                                                                                weight=ft.FontWeight.BOLD
                                                                            )
                                                                        ),
                                                                    ]
                                                                )
                                                            ]
                                                        )
                                                    ),
                                                    ft.Container(
                                                        width=264, 
                                                        height=182,
                                                        padding=ft.padding.only(top=20, left=20, right=20, bottom=3),
                                                        bgcolor=ft.colors.WHITE,
                                                        border_radius=ft.border_radius.all(30),
                                                        margin=ft.margin.only(bottom=10, right=10, left=10, top=0),
                                                        content=ft.Column(
                                                            controls=[
                                                                    ft.Row(
                                                                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                                                        vertical_alignment=ft.CrossAxisAlignment.START,
                                                                        controls=[
                                                                            ft.Text(
                                                                            value="humidity",
                                                                            style=ft.TextStyle(
                                                                                    font_family="IBM Plex Mono",
                                                                                    size=18,
                                                                                    weight=ft.FontWeight.BOLD,
                                                                                    color="#B2B2B2"
                                                                                ),
                                                                            ),
                                                                            ft.Image(
                                                                                src=f"{location}humid.png",
                                                                                height=50,
                                                                                width=50,
                                                                                fit=ft.ImageFit.FIT_HEIGHT,
                                                                            ),

                                                                        ]
                                                                    ),
                                                                    
                                                            
                                                                ft.Text(
                                                                    value=f"{oneCallData['humidity']}",
                                                                    style=ft.TextStyle(
                                                                        font_family="Azeret Mono",
                                                                        size=76,
                                                                        letter_spacing=-6,
                                                                    ),
                                                                    spans=[
                                                                        ft.TextSpan(
                                                                            text=" %",
                                                                            style=ft.TextStyle(
                                                                                font_family="Azeret Mono",
                                                                                size=24, 
                                                                                color="#B2B2B2",
                                                                                letter_spacing=-6,
                                                                                weight=ft.FontWeight.BOLD
                                                                            )
                                                                        ),
                                                                    ]
                                                                )
                                                            ]
                                                        )
                                                    ),
                                                    ft.Container(
                                                        width=264, 
                                                        height=182,
                                                        padding=ft.padding.only(top=20, left=20, right=20, bottom=3),
                                                        bgcolor=ft.colors.WHITE,
                                                        border_radius=ft.border_radius.all(30),
                                                        margin=ft.margin.only(bottom=10, right=10, left=10, top=0),
                                                        content=ft.Column(
                                                            controls=[
                                                                ft.Text(
                                                                    value="set & rise",
                                                                    style=ft.TextStyle(
                                                                        font_family="IBM Plex Mono",
                                                                        size=18,
                                                                        weight=ft.FontWeight.BOLD,
                                                                        color="#B2B2B2"
                                                                    ),
                                                                ),
                                                                ft.Row(
                                                                    alignment=ft.MainAxisAlignment.START,
                                                                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                                                    controls=[
                                                                        ft.Image(
                                                                            src=f"{location}sunrise.png",
                                                                            height=50,
                                                                            width=50,
                                                                            fit=ft.ImageFit.FIT_HEIGHT,
                                                                        ),
                                                                        ft.Container(width=5),
                                                                        ft.Text(
                                                                            value = f"{sunrise_t}",
                                                                            style=ft.TextStyle(
                                                                                font_family="Azeret Mono",
                                                                                size=24,
                                                                                letter_spacing=-2,
                                                                            )
                                                                        ),
                                                                    ]
                                                                ),
                                                                ft.Row(
                                                                    alignment=ft.MainAxisAlignment.START,
                                                                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                                                    controls=[
                                                                        ft.Image(
                                                                            src=f"{location}sunset.png",
                                                                            height=50,
                                                                            width=50,
                                                                            fit=ft.ImageFit.FIT_HEIGHT,
                                                                        ),
                                                                        ft.Container(width=5),
                                                                        ft.Text(
                                                                            value = f"{sunset_t}",
                                                                            style=ft.TextStyle(
                                                                                font_family="Azeret Mono",
                                                                                size=24,
                                                                                letter_spacing=-2,
                                                                            )
                                                                        ),
                                                                    ]
                                                                ),
                                                            ]
                                                        )
                                                    ),
                                                        
                                                ],
                                            ),
                                            ft.Row(
                                                alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                                                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                                width=820,
                                                controls=[
                                                    
                                                    ft.Container(
                                                        width=264, 
                                                        height=182,
                                                        padding=ft.padding.only(top=20, left=20, right=20, bottom=3),
                                                        bgcolor=ft.colors.WHITE,
                                                        border_radius=ft.border_radius.all(30),
                                                        margin=ft.margin.only(bottom=10, right=10, left=10, top=0),
                                                        content=ft.Column(
                                                            controls=[
                                                                    ft.Row(
                                                                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                                                        vertical_alignment=ft.CrossAxisAlignment.START,
                                                                        controls=[
                                                                            ft.Text(
                                                                            value="wind status",
                                                                            style=ft.TextStyle(
                                                                                    font_family="IBM Plex Mono",
                                                                                    size=18,
                                                                                    weight=ft.FontWeight.BOLD,
                                                                                    color="#B2B2B2"
                                                                                ),
                                                                            ),
                                                                            ft.Image(
                                                                                src=f"{location}wind.png",
                                                                                height=50,
                                                                                width=50,
                                                                                fit=ft.ImageFit.FIT_HEIGHT,
                                                                            ),

                                                                        ]
                                                                    ),
                                                                    
                                                            
                                                                ft.Text(
                                                                    value=f"{round(oneCallData['wind_speed'])}",
                                                                    style=ft.TextStyle(
                                                                        font_family="Azeret Mono",
                                                                        size=76,
                                                                        letter_spacing=-6,
                                                                    ),
                                                                    spans=[
                                                                        ft.TextSpan(
                                                                            text=" m/s",
                                                                            style=ft.TextStyle(
                                                                                font_family="Azeret Mono",
                                                                                size=24, 
                                                                                color="#B2B2B2",
                                                                                letter_spacing=-6,
                                                                                weight=ft.FontWeight.BOLD
                                                                            )
                                                                        ),
                                                                    ]
                                                                )
                                                            ]
                                                        )
                                                    ),
                                                    ft.Container(
                                                        width=264, 
                                                        height=182,
                                                        padding=ft.padding.only(top=20, left=20, right=20, bottom=3),
                                                        bgcolor=ft.colors.WHITE,
                                                        border_radius=ft.border_radius.all(30),
                                                        margin=ft.margin.only(bottom=10, right=10, left=10, top=0),
                                                        content=ft.Column(
                                                            controls=[
                                                                    ft.Row(
                                                                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                                                        vertical_alignment=ft.CrossAxisAlignment.START,
                                                                        controls=[
                                                                            ft.Text(
                                                                            value="uv index",
                                                                            style=ft.TextStyle(
                                                                                    font_family="IBM Plex Mono",
                                                                                    size=18,
                                                                                    weight=ft.FontWeight.BOLD,
                                                                                    color="#B2B2B2"
                                                                                ),
                                                                            ),
                                                                            ft.Image(
                                                                                src=f"{location}uv.png",
                                                                                height=50,
                                                                                width=50,
                                                                                fit=ft.ImageFit.FIT_HEIGHT,
                                                                            ),

                                                                        ]
                                                                    ),
                                                                    
                                                            
                                                                ft.Text(
                                                                    value=f"{round(oneCallData['uvi'])}",
                                                                    style=ft.TextStyle(
                                                                        font_family="Azeret Mono",
                                                                        size=76,
                                                                        letter_spacing=-6,
                                                                    ),
                                                                )
                                                            ]
                                                        )
                                                    ),
                                                    ft.Container(
                                                        width=264, 
                                                        height=182,
                                                        padding=ft.padding.only(top=20, left=20, right=20, bottom=3),
                                                        bgcolor=ft.colors.WHITE,
                                                        border_radius=ft.border_radius.all(30),
                                                        margin=ft.margin.only(bottom=10, right=10, left=10, top=0),
                                                        content=ft.Column(
                                                            controls=[
                                                                    ft.Row(
                                                                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                                                        vertical_alignment=ft.CrossAxisAlignment.START,
                                                                        controls=[
                                                                            ft.Text(
                                                                            value="dew point",
                                                                            style=ft.TextStyle(
                                                                                    font_family="IBM Plex Mono",
                                                                                    size=18,
                                                                                    weight=ft.FontWeight.BOLD,
                                                                                    color="#B2B2B2"
                                                                                ),
                                                                            ),
                                                                            ft.Image(
                                                                                src=f"{location}dew.png",
                                                                                height=50,
                                                                                width=50,
                                                                                fit=ft.ImageFit.FIT_HEIGHT,
                                                                            ),

                                                                        ]
                                                                    ),
                                                                    
                                                            
                                                                ft.Text(
                                                                    value=f"{round(oneCallData['dew_point'])}",
                                                                    style=ft.TextStyle(
                                                                        font_family="Azeret Mono",
                                                                        size=76,
                                                                        letter_spacing=-6,
                                                                    ),
                                                                    spans=[
                                                                        ft.TextSpan(
                                                                            text=" °C",
                                                                            style=ft.TextStyle(
                                                                                font_family="Azeret Mono",
                                                                                size=24, 
                                                                                color="#B2B2B2",
                                                                                letter_spacing=-6,
                                                                                weight=ft.FontWeight.BOLD
                                                                            )
                                                                        ),
                                                                    ]
                                                                )
                                                            ]
                                                        )
                                                    ),
                                                    
                                                        
                                                ],
                                            ),

                                        ]    
                                    ),
                                ]
                            )
                        ),
                    ]
                )
            )
            
            print(len(daily_tile))
            
            
            page.clean()
            page.add(weather_frame)
            page.update()
        except:
            page.clean()
            page.add(error_frame)
            page.update()
            
    location_textfield = ft.CupertinoTextField(
            placeholder_text="Search",
            on_submit=apimain_t,
            text_style=ft.TextStyle(color=ft.colors.BLACK87, size=16),
            placeholder_style=ft.TextStyle(color=ft.colors.BLACK45,size=16 ), 
            bgcolor=white_grey,
            height=40,
            border_radius=ft.border_radius.all(8),
            width=350, 
            content_padding=12,
            cursor_color=ft.colors.BLACK,
            suffix=ft.Container(height=30, width=30,
                content=ft.Row(
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Icon(name=ft.cupertino_icons.SEARCH, color=ft.colors.BLACK45, size=20),
                        ft.Container(width=5),
                    ]
                )
            ),
            prefix_visibility_mode=ft.VisibilityMode.ALWAYS,
        )
    
    weather_frame = ft.Container(
        animate=ft.animation.Animation(1000, ft.AnimationCurve.EASE_IN_OUT),
        opacity=50,
        bgcolor="#F7F7F7",
        content=ft.Row(
            alignment=ft.MainAxisAlignment.START,
            vertical_alignment=ft.CrossAxisAlignment.START,
            controls=[
                ft.Container(
                    width=294,
                    padding=ft.padding.all(20),
                    height=page.window_height,
                    bgcolor=ft.colors.WHITE,
                    shadow=ft.BoxShadow(
                                    spread_radius=-80,
                                    blur_radius=50,
                                    color="#b3b3b3"
                                ),
                    content=ft.Column(
                        controls=[
                            ft.Text(
                                text_align=ft.TextAlign.START,
                                value =f"{oneCallData['city']}",
                                style=ft.TextStyle(
                                    weight=ft.FontWeight.W_700,
                                    size=36,
                                    letter_spacing=-2,
                                )
                            ),
                            ft.Container(
                                height=5,
                            ),
                            ft.Image(
                                src=f"{location}01d.png",
                                width=264, 
                                height=210,
                                fit=ft.ImageFit.CONTAIN
                            ),
                            ft.Container(
                                height=10    
                            ),
                            ft.Text(
                                value="36°C",
                                style=ft.TextStyle(
                                    font_family="IBM Plex Mono",
                                    size=64, 
                                    letter_spacing=-5,
                                    weight=ft.FontWeight.BOLD,
                                    height=0.8,
                                )
                            ),
                            ft.Text(
                               value = "Monday",
                                style=ft.TextStyle(
                                    font_family="IBM Plex Mono",
                                    size=24,
                                    letter_spacing=-1,
                                    weight=ft.FontWeight.BOLD,
                                ),
                                spans=[
                                        ft.TextSpan(
                                            text = ", 8 April",
                                            style=ft.TextStyle(
                                                font_family="IBM Plex Mono", 
                                                size=24,
                                                letter_spacing=-1,
                                                weight=ft.FontWeight.NORMAL
                                            )
                                        )
                                    ],
                            ),
                            ft.Divider(
                                height=20,
                                color="#6B6B6B" 
                            ),
                            ft.Text(
                                value="Clear Sky",
                                style=ft.TextStyle(
                                    size=18,
                                    weight=ft.FontWeight.BOLD,
                                    letter_spacing=-1,
                                ),
                            ),
                            ft.Row(
                                alignment=ft.MainAxisAlignment.START,
                                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                controls=[
                                    ft.Image(
                                        src=f"{location}gauge.png",
                                        height=22,
                                        width=22,
                                        fit=ft.ImageFit.FIT_HEIGHT,
                                    ),
                                    ft.Text(
                                        "Pressure:",
                                        style=ft.TextStyle(
                                            font_family="IBM Plex Mono",
                                            size=18,
                                            letter_spacing=-1,
                                            height=0.8,
                                            weight=ft.FontWeight.BOLD
                                        ),
                                        spans=[
                                            ft.TextSpan(
                                                text = " 1094kPa",
                                                style=ft.TextStyle(
                                                    size=18,
                                                    weight=ft.FontWeight.NORMAL
                                                ),
                                            )
                                        ]
                                    ),
                                ],
                            ),
                            ft.Container(
                                height=0,    
                            ),
                            ft.Container(
                                height=160,
                                width=254,
                                border_radius=ft.border_radius.all(20),
                                bgcolor="#F6F6F6",
                                content=ft.Image(
                                    src=f"{location}rainy.jpg",
                                    fit=ft.ImageFit.FIT_HEIGHT
                                ),
                            )
                        ]
                    ),
                ),
                ft.Container(
                    height=page.window_height,
                    bgcolor="#F7F7F7",
                    padding=ft.padding.all(20),
                    alignment=ft.alignment.top_center,
                    
                    content=ft.Column(
                        alignment=ft.MainAxisAlignment.START,
                        controls=[
                            
                            ft.Text(
                                "Daily",
                                style=ft.TextStyle(
                                    font_family="IBM Plex Mono",
                                    size=24,
                                    weight=ft.FontWeight.BOLD,
                                    letter_spacing=-1,
                                    
                                ),
                                spans=[
                                    ft.TextSpan(
                                        text=" Analysis",
                                        style=ft.TextStyle(
                                            font_family="IBM Plex Mono",
                                            size=24,
                                            weight=ft.FontWeight.NORMAL,
                                            letter_spacing=-1,
                                        ),
                                    )
                                ]
                            ),
                            ft.Container(
                                border_radius=ft.border_radius.all(20),
                                height=161,
                                padding=ft.padding.symmetric(vertical=0, horizontal=10),
                                shadow=ft.BoxShadow(
                                    spread_radius=-50,
                                    blur_radius=100,
                                    color="#b3b3b3"
                                ),
                                width=845,
                                bgcolor=ft.colors.WHITE,
                                content=daily_analysis_row,
                            ),
                            ft.Container(
                                height=10,
                            ),
                            ft.Text(
                                "Current",
                                style=ft.TextStyle(
                                    font_family="IBM Plex Mono",
                                    size=24,
                                    weight=ft.FontWeight.BOLD,
                                    letter_spacing=-1,
                                    
                                ),
                                spans=[
                                    ft.TextSpan(
                                        text=" Parameters",
                                        style=ft.TextStyle(
                                            font_family="IBM Plex Mono",
                                            size=24,
                                            weight=ft.FontWeight.NORMAL,
                                            letter_spacing=-1,
                                        ),
                                    )
                                ]
                            ),
                            ft.Column(
                                alignment=ft.MainAxisAlignment.CENTER,
                                horizontal_alignment=ft.CrossAxisAlignment.START,
                                controls=[
                                    ft.Row(
                                        alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                        width=820,
                                        controls=[
                                            
                                            ft.Container(
                                                width=264, 
                                                height=182,
                                                padding=ft.padding.only(top=20, left=20, right=20, bottom=3),
                                                bgcolor=ft.colors.WHITE,
                                                border_radius=ft.border_radius.all(30),
                                                margin=ft.margin.only(bottom=10, right=10, left=10, top=0),
                                                content=ft.Column(
                                                    controls=[
                                                            ft.Row(
                                                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                                                vertical_alignment=ft.CrossAxisAlignment.START,
                                                                controls=[
                                                                    ft.Text(
                                                                    value="visibility",
                                                                    style=ft.TextStyle(
                                                                            font_family="IBM Plex Mono",
                                                                            size=18,
                                                                            weight=ft.FontWeight.BOLD,
                                                                            color="#B2B2B2"
                                                                        ),
                                                                    ),
                                                                    ft.Image(
                                                                        src=f"{location}vis.png",
                                                                        height=50,
                                                                        width=50,
                                                                        fit=ft.ImageFit.FIT_HEIGHT,
                                                                    ),

                                                                ]
                                                            ),
                                                            
                                                    
                                                        ft.Text(
                                                            value="100",
                                                            style=ft.TextStyle(
                                                                font_family="Azeret Mono",
                                                                size=76,
                                                                letter_spacing=-6,
                                                            ),
                                                            spans=[
                                                                ft.TextSpan(
                                                                    text=" km",
                                                                    style=ft.TextStyle(
                                                                        font_family="Azeret Mono",
                                                                        size=24, 
                                                                        color="#B2B2B2",
                                                                        letter_spacing=-6,
                                                                        weight=ft.FontWeight.BOLD
                                                                    )
                                                                ),
                                                            ]
                                                        )
                                                    ]
                                                )
                                            ),
                                            ft.Container(
                                                width=264, 
                                                height=182,
                                                padding=ft.padding.only(top=20, left=20, right=20, bottom=3),
                                                bgcolor=ft.colors.WHITE,
                                                border_radius=ft.border_radius.all(30),
                                                margin=ft.margin.only(bottom=10, right=10, left=10, top=0),
                                                content=ft.Column(
                                                    controls=[
                                                            ft.Row(
                                                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                                                vertical_alignment=ft.CrossAxisAlignment.START,
                                                                controls=[
                                                                    ft.Text(
                                                                    value="humidity",
                                                                    style=ft.TextStyle(
                                                                            font_family="IBM Plex Mono",
                                                                            size=18,
                                                                            weight=ft.FontWeight.BOLD,
                                                                            color="#B2B2B2"
                                                                        ),
                                                                    ),
                                                                    ft.Image(
                                                                        src=f"{location}humid.png",
                                                                        height=50,
                                                                        width=50,
                                                                        fit=ft.ImageFit.FIT_HEIGHT,
                                                                    ),

                                                                ]
                                                            ),
                                                            
                                                    
                                                        ft.Text(
                                                            value="54",
                                                            style=ft.TextStyle(
                                                                font_family="Azeret Mono",
                                                                size=76,
                                                                letter_spacing=-6,
                                                            ),
                                                            spans=[
                                                                ft.TextSpan(
                                                                    text=" %",
                                                                    style=ft.TextStyle(
                                                                        font_family="Azeret Mono",
                                                                        size=24, 
                                                                        color="#B2B2B2",
                                                                        letter_spacing=-6,
                                                                        weight=ft.FontWeight.BOLD
                                                                    )
                                                                ),
                                                            ]
                                                        )
                                                    ]
                                                )
                                            ),
                                            ft.Container(
                                                width=264, 
                                                height=182,
                                                padding=ft.padding.only(top=20, left=20, right=20, bottom=3),
                                                bgcolor=ft.colors.WHITE,
                                                border_radius=ft.border_radius.all(30),
                                                margin=ft.margin.only(bottom=10, right=10, left=10, top=0),
                                                content=ft.Column(
                                                    controls=[
                                                        ft.Text(
                                                            value="set & rise",
                                                            style=ft.TextStyle(
                                                                font_family="IBM Plex Mono",
                                                                size=18,
                                                                weight=ft.FontWeight.BOLD,
                                                                color="#B2B2B2"
                                                            ),
                                                        ),
                                                        ft.Row(
                                                            alignment=ft.MainAxisAlignment.START,
                                                            vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                                            controls=[
                                                                ft.Image(
                                                                    src=f"{location}sunrise.png",
                                                                    height=50,
                                                                    width=50,
                                                                    fit=ft.ImageFit.FIT_HEIGHT,
                                                                ),
                                                                ft.Container(width=5),
                                                                ft.Text(
                                                                    value = "6:09 AM",
                                                                    style=ft.TextStyle(
                                                                        font_family="Azeret Mono",
                                                                        size=24,
                                                                        letter_spacing=-2,
                                                                    )
                                                                ),
                                                            ]
                                                        ),
                                                        ft.Row(
                                                            alignment=ft.MainAxisAlignment.START,
                                                            vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                                            controls=[
                                                                ft.Image(
                                                                    src=f"{location}sunset.png",
                                                                    height=50,
                                                                    width=50,
                                                                    fit=ft.ImageFit.FIT_HEIGHT,
                                                                ),
                                                                ft.Container(width=5),
                                                                ft.Text(
                                                                    value = "7:00 PM",
                                                                    style=ft.TextStyle(
                                                                        font_family="Azeret Mono",
                                                                        size=24,
                                                                        letter_spacing=-2,
                                                                    )
                                                                ),
                                                            ]
                                                        ),
                                                    ]
                                                )
                                            ),
                                                
                                        ],
                                    ),
                                    ft.Row(
                                        alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                        width=820,
                                        controls=[
                                            
                                            ft.Container(
                                                width=264, 
                                                height=182,
                                                padding=ft.padding.only(top=20, left=20, right=20, bottom=3),
                                                bgcolor=ft.colors.WHITE,
                                                border_radius=ft.border_radius.all(30),
                                                margin=ft.margin.only(bottom=10, right=10, left=10, top=0),
                                                content=ft.Column(
                                                    controls=[
                                                            ft.Row(
                                                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                                                vertical_alignment=ft.CrossAxisAlignment.START,
                                                                controls=[
                                                                    ft.Text(
                                                                    value="wind status",
                                                                    style=ft.TextStyle(
                                                                            font_family="IBM Plex Mono",
                                                                            size=18,
                                                                            weight=ft.FontWeight.BOLD,
                                                                            color="#B2B2B2"
                                                                        ),
                                                                    ),
                                                                    ft.Image(
                                                                        src=f"{location}wind.png",
                                                                        height=50,
                                                                        width=50,
                                                                        fit=ft.ImageFit.FIT_HEIGHT,
                                                                    ),

                                                                ]
                                                            ),
                                                            
                                                    
                                                        ft.Text(
                                                            value="21",
                                                            style=ft.TextStyle(
                                                                font_family="Azeret Mono",
                                                                size=76,
                                                                letter_spacing=-6,
                                                            ),
                                                            spans=[
                                                                ft.TextSpan(
                                                                    text=" m/s",
                                                                    style=ft.TextStyle(
                                                                        font_family="Azeret Mono",
                                                                        size=24, 
                                                                        color="#B2B2B2",
                                                                        letter_spacing=-6,
                                                                        weight=ft.FontWeight.BOLD
                                                                    )
                                                                ),
                                                            ]
                                                        )
                                                    ]
                                                )
                                            ),
                                            ft.Container(
                                                width=264, 
                                                height=182,
                                                padding=ft.padding.only(top=20, left=20, right=20, bottom=3),
                                                bgcolor=ft.colors.WHITE,
                                                border_radius=ft.border_radius.all(30),
                                                margin=ft.margin.only(bottom=10, right=10, left=10, top=0),
                                                content=ft.Column(
                                                    controls=[
                                                            ft.Row(
                                                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                                                vertical_alignment=ft.CrossAxisAlignment.START,
                                                                controls=[
                                                                    ft.Text(
                                                                    value="uv index",
                                                                    style=ft.TextStyle(
                                                                            font_family="IBM Plex Mono",
                                                                            size=18,
                                                                            weight=ft.FontWeight.BOLD,
                                                                            color="#B2B2B2"
                                                                        ),
                                                                    ),
                                                                    ft.Image(
                                                                        src=f"{location}uv.png",
                                                                        height=50,
                                                                        width=50,
                                                                        fit=ft.ImageFit.FIT_HEIGHT,
                                                                    ),

                                                                ]
                                                            ),
                                                            
                                                    
                                                        ft.Text(
                                                            value="5",
                                                            style=ft.TextStyle(
                                                                font_family="Azeret Mono",
                                                                size=76,
                                                                letter_spacing=-6,
                                                            ),
                                                        )
                                                    ]
                                                )
                                            ),
                                            ft.Container(
                                                width=264, 
                                                height=182,
                                                padding=ft.padding.only(top=20, left=20, right=20, bottom=3),
                                                bgcolor=ft.colors.WHITE,
                                                border_radius=ft.border_radius.all(30),
                                                margin=ft.margin.only(bottom=10, right=10, left=10, top=0),
                                                content=ft.Column(
                                                    controls=[
                                                            ft.Row(
                                                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                                                vertical_alignment=ft.CrossAxisAlignment.START,
                                                                controls=[
                                                                    ft.Text(
                                                                    value="dew point",
                                                                    style=ft.TextStyle(
                                                                            font_family="IBM Plex Mono",
                                                                            size=18,
                                                                            weight=ft.FontWeight.BOLD,
                                                                            color="#B2B2B2"
                                                                        ),
                                                                    ),
                                                                    ft.Image(
                                                                        src=f"{location}dew.png",
                                                                        height=50,
                                                                        width=50,
                                                                        fit=ft.ImageFit.FIT_HEIGHT,
                                                                    ),

                                                                ]
                                                            ),
                                                            
                                                    
                                                        ft.Text(
                                                            value="54",
                                                            style=ft.TextStyle(
                                                                font_family="Azeret Mono",
                                                                size=76,
                                                                letter_spacing=-6,
                                                            ),
                                                            spans=[
                                                                ft.TextSpan(
                                                                    text=" %",
                                                                    style=ft.TextStyle(
                                                                        font_family="Azeret Mono",
                                                                        size=24, 
                                                                        color="#B2B2B2",
                                                                        letter_spacing=-6,
                                                                        weight=ft.FontWeight.BOLD
                                                                    )
                                                                ),
                                                            ]
                                                        )
                                                    ]
                                                )
                                            ),
                                            
                                                
                                        ],
                                    ),

                                ]    
                            ),
                        ]
                    )
                ),
            ]
        )
    )
    
    init_frame = ft.Container(
            height=680, 
            width=1200, 
            alignment=ft.alignment.center,
            content=ft.Column(
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Image(
                        src=f"{location}nothing.png",
                        height=100,
                        width=100,
                        fit=ft.ImageFit.FIT_HEIGHT
                    ),
                    ft.Container(
                        height=5    
                    ),
                    ft.Text(
                        value = "Search a Location",
                        style = ft.TextStyle(
                            font_family="SF Pro Display",
                            size=18,
                            color="#A7A7A7"
                        )
                    ),
                ]
            )
        )

    page.appbar = ft.AppBar(
        bgcolor=white,
            title=location_textfield,
            center_title=True,
            elevation=1,
            toolbar_height=60,
    )
    
    page.add(init_frame)
    
ft.app(target=main)