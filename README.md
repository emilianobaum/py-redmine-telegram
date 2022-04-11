
El bot debe ser parte del grupo de difusion

Ejemplo obteniendo el chat id para el ot telegram

https://api.telegram.org/bot5250509573:AAGqAfn6OMu7p2SnWCSzVGhaVHUvtDqVNCQ/sendMessage?chat_id=@cgss_eng_team&text=123

Resultado

{

    "ok": true,
    "result": {
        "message_id": 2,
        "sender_chat": {
            "id": -1001562929409,
            "title": "cgss_eng",
            "username": "cgss_eng_team",
            "type": "channel"
        },
        "chat": {
            "id": -1001562929409,
            "title": "cgss_eng",
            "username": "cgss_eng_team",
            "type": "channel"
        },
        "date": 1649371068,
        "text": "123"
    }

}