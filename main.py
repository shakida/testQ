# Beta version
# By me (tg-@shakida69)
import os
import re
from pyrogram import Client, filters, idle
from pyrogram.types import Message
from pyrogram.raw import functions, types
import pyrogram
from os import path
import uuid
import subprocess
from typing import Union
import asyncio
import wget
import math
import os, time, asyncio, json
import time
from datetime import datetime
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import psutil
from psutil._common import bytes2human
self_or_contact_filter = filters.create(
    lambda _, __, message: (message.from_user and message.from_user.is_contact)
    or message.outgoing
)
import wget

shakida = Client(
    ":memory:",
    '2177518',
    '6f700167aeed1f5d546eab443e85bd7d',
    bot_token='2132740464:AAECc8VJBu4nx0Q4vsNYUaD5JL-Ey_BN4z0')
shakida.start()
shakida.send_message(-1001297289773, f'🍑 Alive')
temp = []
boot_time = time.time()

def humanbytes(size):
    if not size:
        return ""
    power = 2 ** 10
    raised_to_pow = 0
    dict_power_n = {0: "", 1: "Ki", 2: "Mi", 3: "Gi", 4: "Ti"}
    while size > power:
        size /= power
        raised_to_pow += 1
    return str(round(size, 2)) + " " + dict_power_n[raised_to_pow] + "B"

def get_readable_time(seconds: int) -> str:
    result = ''
    (days, remainder) = divmod(seconds, 86400)
    days = int(days)
    if days != 0:
        result += f'{days}d'
    (hours, remainder) = divmod(remainder, 3600)
    hours = int(hours)
    if hours != 0:
        result += f'{hours}h'
    (minutes, seconds) = divmod(remainder, 60)
    minutes = int(minutes)
    if minutes != 0:
        result += f'{minutes}m'
    seconds = int(seconds)
    result += f'{seconds}s'
    return result

def TimeFormatter(milliseconds: int) -> str:
    seconds, milliseconds = divmod(int(milliseconds), 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    tmp = ((str(days) + "d, ") if days else "") + \
        ((str(hours) + "h, ") if hours else "") + \
        ((str(minutes) + "m, ") if minutes else "") + \
        ((str(seconds) + "s, ") if seconds else "")
    return tmp[:-2]
    

        
@shakida.on_message(filters.command(["compo", "compo@svidcompo_bot"]) & filters.group)
async def compox(s: shakida, message: Message):
          global temp
          tempid = uuid.uuid4()
          video = message.reply_to_message
          any = message.from_user.id
          if video is None:
             await s.send_message(message.chat.id, f'**No video provided ‼️')
             return
          else:
             f = await s.send_message(message.chat.id, f"**🔄 Prosesing**")
             if len(message.command) != 2:
                crf = 27
             if len(message.command) == 2:
                crf = int(message.text.split(None)[1])
             if (crf < 20) or (crf > 50):
                await f.edit(f'**ERROR!**\nCRF 20-50 value only or default 27')
                return
             file_n = video.video.file_name
             ch = video.video.mime_type.split('/')[1]
             duration = video.video.duration
             file_s = video.video.file_size
             height = video.video.height
             width = video.video.width
             file = f'{video.video.file_unique_id}.mkv'
             v = f"downloads/{file}"
             pic = f'{tempid}Thumb.png'
             deu = duration / 2
             butt = InlineKeyboardMarkup([[InlineKeyboardButton("⚙️ Status", callback_data=f"sys"),]])
             temp.append(str(file))
             heh = f'**🏷️ File Name:** `{file_n}`\n**📥 DOWNLOADING...**\n'
             hah = f'**🍻 CC:** {message.from_user.first_name}'
             await f.edit(f'{heh}{hah}', reply_markup=butt, disable_web_page_preview=True)
             try:
                videox = await video.download(file)
             except Exception as e:
                temp.pop(0)
                await f.edit(f'**ERROR!!: Downloading error.\n`{e}`')
                return
             try:
              #  compo = time.time()
                doss = int(15)
                px = await asyncio.create_subprocess_shell(
                f'ffmpeg -hide_banner -loglevel quiet -i "{v}" -preset ultrafast -vcodec libx265 -crf {crf} "{file}" -y',
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE,
                )
                pxp = await asyncio.create_subprocess_shell(
                f"ffmpeg -i {v} -ss {deu} -vframes 1 {pic}",
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE,
                )
                but = InlineKeyboardMarkup([[
                InlineKeyboardButton("❌ Cancel", callback_data=f'cl {file}|{crf}|{any}'),
                InlineKeyboardButton("⚙️ Status", callback_data=f"sys"),
                ]])
                await f.edit(f'**🏷️ File Name:** ` {file_n}`\n**🗜️ COMPRESSING...**\n**⚙️ CRF Range:** `{crf}`\n'
                + f'**🍻 CC:** {message.from_user.first_name}',
                reply_markup=but, disable_web_page_preview=True)
                try:
                    await px.communicate()
                except Exception as e:
                    temp.pop(0)
                    await f.edit(f'**ERROR!!:** {e}`')
                    return
                try:
                    await pxp.communicate()
                except Exception as e:
                    temp.pop(0)
                    await f.edit(f'**ERROR!!:** {e}`')
                    return
                os.remove(f'{v}')
                await f.edit(f'**🏷️ File Name:** `{file_n}`\n**COMPRESSION DONE ✅**\n**📤 File Uploading...**\n'
                + f'**🍻 CC:** {message.from_user.first_name}', reply_markup=but,  disable_web_page_preview=True)
                await video.reply_video(video=file, thumb=pic, supports_streaming=True, duration=duration, height=height, width=width, caption=f'**🏷️ File Name: `{file_n}`'
                + f'\n**🚦 Preset:** `Ultrafast`\n**⚙️ CRF:** `{crf}`\n'
                + f'**💾 Orginal size:** `{humanbytes(file_s)}`\n'
                + f'**🍻 CC:** {message.from_user.first_name}')
                await f.delete()
                os.remove(f'{file}')
                os.remove(f'{pic}')
                temp.pop(0)
             #   os.remove(pic)
             except Exception as a:
                temp.pop(0)
                print(a)
                return

@shakida.on_message(filters.command(["sample", "sample@svidcompo_bot"]) & filters.group)
async def samplex(s: shakida, message: Message):
      global temp
      tempidx = uuid.uuid4()
      video = message.reply_to_message
      any = message.from_user.id
      if video is None:
          await s.send_message(message.chat.id, f'**No video provided ‼️')
          return
      else:
          durationx = video.video.duration
          heightx = video.video.height
          widthx = video.video.width
          filep = f'{video.video.file_unique_id}.mkv'
          picx = f'{tempidx}pThumb.png'
          deux = durationx / 2
          x = round(durationx / 5)
          y = round(durationx / 5 + 30)
          skk = x
          if y < durationx:
             dkk = y
          if y > durationx:
             dkk = durationx
          f = await s.send_message(message.chat.id, f"🔄 Making Sample video...")
          file_p = video.video.file_name
          try:
             temp.append(str(filep))
             await f.edit(f"**Downloading.. 📥**")
             vidxp = await video.download(filep)
          except Exception as e:
             temp.pop(0)
             await f.edit(f'**ERROR!: Downloading error.\n`{e}`')
             return
          try:
             await f.edit(f'**Trying to make sample video 📽️**')
             try:
                sample_m = f"ffmpeg -ss {skk} -to {dkk} -i {vidxp} -c copy {filep}"
                pro = await asyncio.create_subprocess_shell(
                sample_m,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE,
                )
                await pro.communicate()
             except Exception as e:
                temp.pop(0)
                os.remove(f'{filep}')
                await f.edit(f'**ERROR!:**\n`{e}`')
                return
             try:
                procx = await asyncio.create_subprocess_shell(
                    f"ffmpeg -i {filep} -ss {deux} -vframes 1 {picx}",
                    stdout=asyncio.subprocess.PIPE,
                    stderr=asyncio.subprocess.PIPE,
                    )
                await procx.communicate()
             except Exception as e:
                temp.pop(0)
                os.remove(f'{picx}')
                await f.edit(f'**ERROR!!:** {e}`')
                return
             os.remove(f'{vidxp}')
             await f.edit(f'Sample created successfully. Uploading..')
             await video.reply_video(video=filep, thumb=picx, supports_streaming=True, height=heightx, width=widthx, caption=f'**🏷️ File Name: `{file_p}`'
                + f'\n**〽️ Sample video:** {skk} - {dkk}`\n'
                + f'🍻 CC: {message.from_user.first_name}',)
             await f.delete()
             os.remove(f'{filep}')
             temp.pop(0)
             os.remove(f'{picx}')
          except Exception as a:
             temp.pop(0)
             os.remove(f'{picx}')
             print(a)
             return

@shakida.on_callback_query(
    filters.regex(pattern=r"cl")
)
async def callb(shakida, cb):
 #   chet_id = cb.message.chat.id
    global temp
    cbd = cb.data.strip()
    bu = InlineKeyboardMarkup([[InlineKeyboardButton("⚙️ Status", callback_data=f"sys"),]])
    typed_=cbd.split(None, 1)[1]
    try:
       file, crf, any= typed_.split("|")
    except Exception as e:
       print(e)
       return
    sudo = int(875645659)
    useer_id = int(any)
    if cb.from_user.id != useer_id:
        await cb.answer("❌ Not for you.", show_alert=True)
        return
    try:
       os.remove(file)
       temp.pop(0)
       await cb.message.edit(f'**❌ STOPPED OPERATION**\n**⚙️ CRF RANGE:** {crf}\n'
       + f'**🍻 CC:** {cb.from_user.mention()}',
       reply_markup=bu)
    except Exception as e:
       await cb.message.edit(f'**Nothing to stopped ‼️**\n**Reason:** `{e}`', reply_markup=bu)
       return
@shakida.on_callback_query(filters.regex(pattern=r"^(sys)$"))
async def sya(shakida, cb):
     global temp
     list = len(temp)
     type_ = cb.matches[0].group(1)
   #   the_data = cb.message.reply_markup.inline_keyboard[1][0].callback_data
   #  by = cb.from_user.first_name
   #  userr = cb.from_user.id
     if type_ == "sys":
      #    await cb.answer(f"❌ Close by {by}")
      #    LOGGER.warning("Close button executed")
          ccpu = f"{psutil.cpu_percent(interval=1)}%"
          await cb.answer(f"💡 OPERATION STATUS :\n\n⚙️ CPU USAGE: {ccpu}\n🗜️ #{list} Prosess Running 🟢", show_alert=True)
     return
@shakida.on_message(filters.command("ss") & filters.group)
async def shell(client: shakida, message: Message):
    cmd = message.text.split(' ', 1)
    if len(cmd) == 1:
        await message.reply_text('**No command to execute was given!**')
        return
    cmd = cmd[1]
    process = subprocess.Popen(
        cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    stdout, stderr = process.communicate()
    reply = ''
    stderr = stderr.decode()
    stdout = stdout.decode()
    if stdout:
        reply += f"⚙️**Stdout**\n`{stdout}`\n"
    if stderr:
        reply += f"⚙️**Stderr**\n`{stderr}`\n"
    if len(reply) > 3000:
        with open('shell_output.txt', 'w') as file:
            file.write(reply)
        with open('shell_output.txt', 'rb') as doc:
            client.send_document(
                document=doc,
                filename=doc.name,
                reply_to_message_id=message.message_id,
                chat_id=message.chat_id)
    else:
        await message.reply_text(reply)


async def generate_sysinfo(workdir):
    # uptime
    info = {}
    info["🔌boot"] = datetime.fromtimestamp(psutil.boot_time()).strftime(
        "%Y-%m-%d %H:%M:%S"
    )
    # CPU
    cpu_freq = psutil.cpu_freq().current
    if cpu_freq >= 1000:
        cpu_freq = f"{round(cpu_freq / 1000, 2)}GHz"
    else:
        cpu_freq = f"{round(cpu_freq, 2)}MHz"
    info["🌡️cpu"] = (
        f" {psutil.cpu_percent(interval=1)}% " f"({psutil.cpu_count()}) " f"{cpu_freq}"
    )
    # Memory
    vm = psutil.virtual_memory()
    sm = psutil.swap_memory()
    info["💾ram"] = f"{bytes2human(vm.total)}, " f"{bytes2human(vm.available)} available"
    info["💽swap"] = f"{bytes2human(sm.total)}, {sm.percent}%"
    # Disks
    du = psutil.disk_usage(workdir)
    dio = psutil.disk_io_counters()
    info["💿disk"] = (
        f"{bytes2human(du.used)} / {bytes2human(du.total)} " f"({du.percent}%)"
    )
    if dio:
        info["📀disk io"] = (
            f"R {bytes2human(dio.read_bytes)} | " f"W {bytes2human(dio.write_bytes)}"
        )
    # Network
    nio = psutil.net_io_counters()
    info["🚀net io"] = (
        f"TX {bytes2human(nio.bytes_sent)} | " f"RX {bytes2human(nio.bytes_recv)}"
    )
    # Sensors
    sensors_temperatures = psutil.sensors_temperatures()
    if sensors_temperatures:
        temperatures_list = [x.current for x in sensors_temperatures["coretemp"]]
        temperatures = sum(temperatures_list) / len(temperatures_list)
        info["🌡️temp"] = f"{temperatures}\u00b0C"
    info = {f"{key}:": value for (key, value) in info.items()}
    max_len = max(len(x) for x in info)
    return "```" + "\n".join([f"{x:<{max_len}} {y}" for x, y in info.items()]) + "```"
    """
    partition_info = []
    for part in psutil.disk_partitions():
        mp = part.mountpoint
        du = psutil.disk_usage(mp)
        partition_info.append(f"{part.device} {mp} "
                              f"{part.fstype} "
                              f"{du.used} / {du.total} {du.percent}")
    partition_info = ",".join(partition_info)
    """


@shakida.on_message(filters.command("cmsys") & filters.group)
async def get_sysinfo(client: shakida, m):
    response = "⚙️ __**System Information:**__\n"
    m_reply = await m.reply_text(f"{response}`...`")
    response += await generate_sysinfo(client.workdir)
    await m_reply.edit_text(response)

@shakida.on_message(filters.command(["ping", "ping@svidcompo_bot"]) & filters.group)
async def ping(client: shakida, message: Message):
       s_time = int(round(time.time() * 1000))
       bo = InlineKeyboardMarkup([[InlineKeyboardButton("⚙️ Status", callback_data=f"sys"),]])
       uptime = get_readable_time(time.time() - boot_time)
       p = await message.reply_text(f'**Checking..**')
       e_time = int(round(time.time() * 1000))
       pingg = int(e_time - s_time)
       await p.edit(f'**PONG 🍑**\n**🏓 Ping:** {pingg}ms\n**⏳ Uptime:** {uptime}', reply_markup=bo)


idle()
