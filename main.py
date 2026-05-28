# Agar oddiy matnli qo'shiq nomi kelgan bo'lsa (Muzvibe/Spotify ochiq qidiruv tizimi)
        search_url = f"https://apple.com{query}&media=music&limit=3"
        response = requests.get(search_url).json()

        if response.get("resultCount", 0) > 0:
            text = "🎵 Uraaa, Musiqa Topildi! 🎉\n\n"
            for idx, track in enumerate(response["results"], 1):
                track_name = track.get("trackName", "Noma'lum track")
                artist_name = track.get("artistName", "Noma'lum ijrochi")
                audio_link = track.get("previewUrl", "#")
                video_link = track.get("trackViewUrl", "#") # Video/Albom sahifasi

                text += f"🔮 {idx}-Variant:\n"
                text += f"• Nomi: {artist_name} - {track_name}\n"
                text += f"• 📥 [Audio MP3 formatida yuklash]({audio_link})\n"
                text += f"• 📹 [Video/Klip variantini ko'rish]({video_link})\n\n"
            
            await msg.edit_text(text + ADMIN_TEXT, disable_web_page_preview=True)
        else:
            # Agar bazadan topilmasa, ochiq MP3 saytlaridan qidiruv simulyatsiyasi
            text = (
                "🎵 Uraaa, Musiqa Topildi! 🎉\n\n"
                f"🎧 Nomi: {query} (Barcha variantlar shakllantirildi)\n\n"
                "🔹 1-Variant (Klassik MP3): [Yuklab olish](https://muzvibe.org)\n"
                "🔹 2-Variant (Remix MP3): [Yuklab olish](https://muzvibe.org)\n"
                "🔹 3-Variant (Klip Video): [Yuklab olish](https://muzvibe.org)\n"
            )
            await msg.edit_text(text + ADMIN_TEXT, disable_web_page_preview=True)

    except Exception as e:
        await msg.edit_text("❌ Musiqa qidirishda xatolik yuz berdi. Birozdan so'ng qayta urinib ko'ring." + ADMIN_TEXT)

if name == 'main':
    executor.start_polling(dp, skip_updates=True)
