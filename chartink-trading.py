import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import html


# Changlog
# Added Indices TSI < 0 crossover indicator
# Re organized the output on telegram

#source : https://www.youtube.com/watch?v=DLqB6ly5k0I

Charting_url ='https://chartink.com/screener/process'

Condition = {'scan_clause' : '( {57960} ( latest {custom_indicator_23679_start}"(  {custom_indicator_22711_start}"ema(  ema(  {custom_indicator_22709_start} "close - 1 candle ago close"{custom_indicator_22709_end} , 25 ) , 13 )"{custom_indicator_22711_end} /  {custom_indicator_22714_start}"ema(  ema(  {custom_indicator_22712_start}"abs(  close - 1 candle ago close )"{custom_indicator_22712_end} , 25 ) , 13 )"{custom_indicator_22714_end} ) * 100"{custom_indicator_23679_end} < 0 and latest {custom_indicator_23680_start}"ema(  {custom_indicator_22715_start} "100 * (  {custom_indicator_22711_start}"ema(  ema(  {custom_indicator_22709_start} "close - 1 candle ago close"{custom_indicator_22709_end} , 25 ) , 13 )"{custom_indicator_22711_end} /  {custom_indicator_22714_start}"ema(  ema(  {custom_indicator_22712_start}"abs(  close - 1 candle ago close )"{custom_indicator_22712_end} , 25 ) , 13 )"{custom_indicator_22714_end} )"{custom_indicator_22715_end} , 13 )"{custom_indicator_23680_end} < 0 and latest {custom_indicator_23679_start}"(  {custom_indicator_22711_start}"ema(  ema(  {custom_indicator_22709_start} "close - 1 candle ago close"{custom_indicator_22709_end} , 25 ) , 13 )"{custom_indicator_22711_end} /  {custom_indicator_22714_start}"ema(  ema(  {custom_indicator_22712_start}"abs(  close - 1 candle ago close )"{custom_indicator_22712_end} , 25 ) , 13 )"{custom_indicator_22714_end} ) * 100"{custom_indicator_23679_end} > latest {custom_indicator_23680_start}"ema(  {custom_indicator_22715_start} "100 * (  {custom_indicator_22711_start}"ema(  ema(  {custom_indicator_22709_start} "close - 1 candle ago close"{custom_indicator_22709_end} , 25 ) , 13 )"{custom_indicator_22711_end} /  {custom_indicator_22714_start}"ema(  ema(  {custom_indicator_22712_start}"abs(  close - 1 candle ago close )"{custom_indicator_22712_end} , 25 ) , 13 )"{custom_indicator_22714_end} )"{custom_indicator_22715_end} , 13 )"{custom_indicator_23680_end} and 1 day ago  {custom_indicator_23679_start}"(  {custom_indicator_22711_start}"ema(  ema(  {custom_indicator_22709_start} "close - 1 candle ago close"{custom_indicator_22709_end} , 25 ) , 13 )"{custom_indicator_22711_end} /  {custom_indicator_22714_start}"ema(  ema(  {custom_indicator_22712_start}"abs(  close - 1 candle ago close )"{custom_indicator_22712_end} , 25 ) , 13 )"{custom_indicator_22714_end} ) * 100"{custom_indicator_23679_end} <= 1 day ago  {custom_indicator_23680_start}"ema(  {custom_indicator_22715_start} "100 * (  {custom_indicator_22711_start}"ema(  ema(  {custom_indicator_22709_start} "close - 1 candle ago close"{custom_indicator_22709_end} , 25 ) , 13 )"{custom_indicator_22711_end} /  {custom_indicator_22714_start}"ema(  ema(  {custom_indicator_22712_start}"abs(  close - 1 candle ago close )"{custom_indicator_22712_end} , 25 ) , 13 )"{custom_indicator_22714_end} )"{custom_indicator_22715_end} , 13 )"{custom_indicator_23680_end} ) ) '}

Exit_Condition = {'scan_clause': '( {57960} ( latest {custom_indicator_23679_start}"(  {custom_indicator_22711_start}"ema(  ema(  {custom_indicator_22709_start} "close - 1 candle ago close"{custom_indicator_22709_end} , 25 ) , 13 )"{custom_indicator_22711_end} /  {custom_indicator_22714_start}"ema(  ema(  {custom_indicator_22712_start}"abs(  close - 1 candle ago close )"{custom_indicator_22712_end} , 25 ) , 13 )"{custom_indicator_22714_end} ) * 100"{custom_indicator_23679_end} > 0 and latest {custom_indicator_23680_start}"ema(  {custom_indicator_22715_start} "100 * (  {custom_indicator_22711_start}"ema(  ema(  {custom_indicator_22709_start} "close - 1 candle ago close"{custom_indicator_22709_end} , 25 ) , 13 )"{custom_indicator_22711_end} /  {custom_indicator_22714_start}"ema(  ema(  {custom_indicator_22712_start}"abs(  close - 1 candle ago close )"{custom_indicator_22712_end} , 25 ) , 13 )"{custom_indicator_22714_end} )"{custom_indicator_22715_end} , 13 )"{custom_indicator_23680_end} > 0 and latest {custom_indicator_23679_start}"(  {custom_indicator_22711_start}"ema(  ema(  {custom_indicator_22709_start} "close - 1 candle ago close"{custom_indicator_22709_end} , 25 ) , 13 )"{custom_indicator_22711_end} /  {custom_indicator_22714_start}"ema(  ema(  {custom_indicator_22712_start}"abs(  close - 1 candle ago close )"{custom_indicator_22712_end} , 25 ) , 13 )"{custom_indicator_22714_end} ) * 100"{custom_indicator_23679_end} < latest {custom_indicator_23680_start}"ema(  {custom_indicator_22715_start} "100 * (  {custom_indicator_22711_start}"ema(  ema(  {custom_indicator_22709_start} "close - 1 candle ago close"{custom_indicator_22709_end} , 25 ) , 13 )"{custom_indicator_22711_end} /  {custom_indicator_22714_start}"ema(  ema(  {custom_indicator_22712_start}"abs(  close - 1 candle ago close )"{custom_indicator_22712_end} , 25 ) , 13 )"{custom_indicator_22714_end} )"{custom_indicator_22715_end} , 13 )"{custom_indicator_23680_end} and 1 day ago  {custom_indicator_23679_start}"(  {custom_indicator_22711_start}"ema(  ema(  {custom_indicator_22709_start} "close - 1 candle ago close"{custom_indicator_22709_end} , 25 ) , 13 )"{custom_indicator_22711_end} /  {custom_indicator_22714_start}"ema(  ema(  {custom_indicator_22712_start}"abs(  close - 1 candle ago close )"{custom_indicator_22712_end} , 25 ) , 13 )"{custom_indicator_22714_end} ) * 100"{custom_indicator_23679_end} >= 1 day ago  {custom_indicator_23680_start}"ema(  {custom_indicator_22715_start} "100 * (  {custom_indicator_22711_start}"ema(  ema(  {custom_indicator_22709_start} "close - 1 candle ago close"{custom_indicator_22709_end} , 25 ) , 13 )"{custom_indicator_22711_end} /  {custom_indicator_22714_start}"ema(  ema(  {custom_indicator_22712_start}"abs(  close - 1 candle ago close )"{custom_indicator_22712_end} , 25 ) , 13 )"{custom_indicator_22714_end} )"{custom_indicator_22715_end} , 13 )"{custom_indicator_23680_end} ) ) '}

Weekly_Entry_Condition = {'scan_clause': '( {57960} ( weekly {custom_indicator_23679_start}"(  {custom_indicator_22711_start}"ema(  ema(  {custom_indicator_22709_start} "close - 1 candle ago close"{custom_indicator_22709_end} , 25 ) , 13 )"{custom_indicator_22711_end} /  {custom_indicator_22714_start}"ema(  ema(  {custom_indicator_22712_start}"abs(  close - 1 candle ago close )"{custom_indicator_22712_end} , 25 ) , 13 )"{custom_indicator_22714_end} ) * 100"{custom_indicator_23679_end} < 0 and weekly {custom_indicator_23680_start}"ema(  {custom_indicator_22715_start} "100 * (  {custom_indicator_22711_start}"ema(  ema(  {custom_indicator_22709_start} "close - 1 candle ago close"{custom_indicator_22709_end} , 25 ) , 13 )"{custom_indicator_22711_end} /  {custom_indicator_22714_start}"ema(  ema(  {custom_indicator_22712_start}"abs(  close - 1 candle ago close )"{custom_indicator_22712_end} , 25 ) , 13 )"{custom_indicator_22714_end} )"{custom_indicator_22715_end} , 13 )"{custom_indicator_23680_end} < 0 and weekly {custom_indicator_23679_start}"(  {custom_indicator_22711_start}"ema(  ema(  {custom_indicator_22709_start} "close - 1 candle ago close"{custom_indicator_22709_end} , 25 ) , 13 )"{custom_indicator_22711_end} /  {custom_indicator_22714_start}"ema(  ema(  {custom_indicator_22712_start}"abs(  close - 1 candle ago close )"{custom_indicator_22712_end} , 25 ) , 13 )"{custom_indicator_22714_end} ) * 100"{custom_indicator_23679_end} > weekly {custom_indicator_23680_start}"ema(  {custom_indicator_22715_start} "100 * (  {custom_indicator_22711_start}"ema(  ema(  {custom_indicator_22709_start} "close - 1 candle ago close"{custom_indicator_22709_end} , 25 ) , 13 )"{custom_indicator_22711_end} /  {custom_indicator_22714_start}"ema(  ema(  {custom_indicator_22712_start}"abs(  close - 1 candle ago close )"{custom_indicator_22712_end} , 25 ) , 13 )"{custom_indicator_22714_end} )"{custom_indicator_22715_end} , 13 )"{custom_indicator_23680_end} and 1 week ago  {custom_indicator_23679_start}"(  {custom_indicator_22711_start}"ema(  ema(  {custom_indicator_22709_start} "close - 1 candle ago close"{custom_indicator_22709_end} , 25 ) , 13 )"{custom_indicator_22711_end} /  {custom_indicator_22714_start}"ema(  ema(  {custom_indicator_22712_start}"abs(  close - 1 candle ago close )"{custom_indicator_22712_end} , 25 ) , 13 )"{custom_indicator_22714_end} ) * 100"{custom_indicator_23679_end} <= 1 week ago  {custom_indicator_23680_start}"ema(  {custom_indicator_22715_start} "100 * (  {custom_indicator_22711_start}"ema(  ema(  {custom_indicator_22709_start} "close - 1 candle ago close"{custom_indicator_22709_end} , 25 ) , 13 )"{custom_indicator_22711_end} /  {custom_indicator_22714_start}"ema(  ema(  {custom_indicator_22712_start}"abs(  close - 1 candle ago close )"{custom_indicator_22712_end} , 25 ) , 13 )"{custom_indicator_22714_end} )"{custom_indicator_22715_end} , 13 )"{custom_indicator_23680_end} ) ) '}

Indice_Daily_Entry_condition = {'scan_clause':'( {45603} ( latest {custom_indicator_23679_start}"(  {custom_indicator_22711_start}"ema(  ema(  {custom_indicator_22709_start} "close - 1 candle ago close"{custom_indicator_22709_end} , 25 ) , 13 )"{custom_indicator_22711_end} /  {custom_indicator_22714_start}"ema(  ema(  {custom_indicator_22712_start}"abs(  close - 1 candle ago close )"{custom_indicator_22712_end} , 25 ) , 13 )"{custom_indicator_22714_end} ) * 100"{custom_indicator_23679_end} < -5 and latest {custom_indicator_23680_start}"ema(  {custom_indicator_22715_start} "100 * (  {custom_indicator_22711_start}"ema(  ema(  {custom_indicator_22709_start} "close - 1 candle ago close"{custom_indicator_22709_end} , 25 ) , 13 )"{custom_indicator_22711_end} /  {custom_indicator_22714_start}"ema(  ema(  {custom_indicator_22712_start}"abs(  close - 1 candle ago close )"{custom_indicator_22712_end} , 25 ) , 13 )"{custom_indicator_22714_end} )"{custom_indicator_22715_end} , 13 )"{custom_indicator_23680_end} < -5 and latest {custom_indicator_23679_start}"(  {custom_indicator_22711_start}"ema(  ema(  {custom_indicator_22709_start} "close - 1 candle ago close"{custom_indicator_22709_end} , 25 ) , 13 )"{custom_indicator_22711_end} /  {custom_indicator_22714_start}"ema(  ema(  {custom_indicator_22712_start}"abs(  close - 1 candle ago close )"{custom_indicator_22712_end} , 25 ) , 13 )"{custom_indicator_22714_end} ) * 100"{custom_indicator_23679_end} > latest {custom_indicator_23680_start}"ema(  {custom_indicator_22715_start} "100 * (  {custom_indicator_22711_start}"ema(  ema(  {custom_indicator_22709_start} "close - 1 candle ago close"{custom_indicator_22709_end} , 25 ) , 13 )"{custom_indicator_22711_end} /  {custom_indicator_22714_start}"ema(  ema(  {custom_indicator_22712_start}"abs(  close - 1 candle ago close )"{custom_indicator_22712_end} , 25 ) , 13 )"{custom_indicator_22714_end} )"{custom_indicator_22715_end} , 13 )"{custom_indicator_23680_end} and 1 day ago  {custom_indicator_23679_start}"(  {custom_indicator_22711_start}"ema(  ema(  {custom_indicator_22709_start} "close - 1 candle ago close"{custom_indicator_22709_end} , 25 ) , 13 )"{custom_indicator_22711_end} /  {custom_indicator_22714_start}"ema(  ema(  {custom_indicator_22712_start}"abs(  close - 1 candle ago close )"{custom_indicator_22712_end} , 25 ) , 13 )"{custom_indicator_22714_end} ) * 100"{custom_indicator_23679_end} <= 1 day ago  {custom_indicator_23680_start}"ema(  {custom_indicator_22715_start} "100 * (  {custom_indicator_22711_start}"ema(  ema(  {custom_indicator_22709_start} "close - 1 candle ago close"{custom_indicator_22709_end} , 25 ) , 13 )"{custom_indicator_22711_end} /  {custom_indicator_22714_start}"ema(  ema(  {custom_indicator_22712_start}"abs(  close - 1 candle ago close )"{custom_indicator_22712_end} , 25 ) , 13 )"{custom_indicator_22714_end} )"{custom_indicator_22715_end} , 13 )"{custom_indicator_23680_end} ) ) '}

with requests.session() as s:
    r_data = s.get(Charting_url)
    soup = bs(r_data.content, "lxml")
    meta = soup.find("meta",{"name" : "csrf-token"})["content"]


header = {"X-Csrf-Token" : meta}

# Fetching Entry Stock
data = s.post(Charting_url, headers=header, data=Condition).json()
stock_list = pd.DataFrame(data["data"])
print (stock_list)
telegram_output = stock_list

# Fetching Exit Stocks
data = s.post(Charting_url, headers=header, data=Exit_Condition).json()
exit_stock_list = pd.DataFrame(data["data"])
print (exit_stock_list)
exit_telegram_output = exit_stock_list

# Fetching WEEKLY Entry Stock
data = s.post(Charting_url, headers=header, data=Weekly_Entry_Condition).json()
weekly_tsi_entry_stock_list = pd.DataFrame(data["data"])
print (weekly_tsi_entry_stock_list)
weekly_tsi_entry_stock_list_telegram_output = weekly_tsi_entry_stock_list

# Fetching Indices Entry Stock
data = s.post(Charting_url, headers=header, data=Indice_Daily_Entry_condition).json()
indices_entry_stock_list = pd.DataFrame(data["data"])


# Select the desired columns for Entry stocks
filtered_stock_list = stock_list[['sr', 'nsecode', 'close']]
print(filtered_stock_list)

# Select the desired columns for Exit stocks
exit_filtered_stock_list = exit_stock_list[['sr', 'nsecode', 'close']]
print(exit_filtered_stock_list)

# Select the desired columns for Exit stocks
weekly_tsi_entry_stock_list_filtered = weekly_tsi_entry_stock_list[['sr', 'nsecode', 'close']]
print(weekly_tsi_entry_stock_list_filtered)

# Select the desired columns for Indices Entry stocks
indices_entry_stock_list_filtered = indices_entry_stock_list[['sr', 'nsecode', 'close']]
print(indices_entry_stock_list_filtered)



# --- Notification helpers: Telegram + Discord (embeds) ---

def clip_cell(text: str, width: int) -> str:
    s = str(text)
    if len(s) <= width:
        return s
    if width <= 1:
        return s[:width]
    return s[: width - 1] + "…"


def compute_widths(df: pd.DataFrame, columns, caps):
    widths = []
    for col in columns:
        header_len = len(str(col))
        if df is None or df.empty:
            max_data_len = 0
        else:
            max_data_len = int(df[col].astype(str).map(len).max())
        cap = caps.get(col, max(header_len, max_data_len))
        width = min(max(header_len, max_data_len), cap)
        widths.append(width)
    return widths


def build_fixed_table(df: pd.DataFrame, columns=("sr", "nsecode", "close")) -> str:
    """Return a left-aligned, fixed-width ASCII table for the given df.
    Includes a header row and a separator row. Truncates overly long cells.
    """
    try:
        if df is None or df.empty:
            # Still show headers for consistency
            tmp = pd.DataFrame(columns=list(columns))
            df = tmp
        # Keep only required columns and stringify
        safe_df = df.loc[:, list(columns)].copy()
        # Left alignment for all as strings; format close consistently if present
        if "close" in safe_df.columns:
            safe_df["close"] = safe_df["close"].apply(lambda x: str(x))
        for c in safe_df.columns:
            safe_df[c] = safe_df[c].astype(str)

        # Column caps to keep lines reasonable
        caps = {"sr": 6, "nsecode": 24, "close": 14}
        widths = compute_widths(safe_df, columns, caps)

        # Build header and separator
        header_cells = [str(col).ljust(w) for col, w in zip(columns, widths)]
        header_line = " | ".join(header_cells)
        sep_line = "-+-".join("-" * w for w in widths)

        # Build rows
        lines = [header_line, sep_line]
        for _, row in safe_df.iterrows():
            cells = [clip_cell(row[col], w).ljust(w) for col, w in zip(columns, widths)]
            lines.append(" | ".join(cells))
        return "\n".join(lines)
    except Exception as e:
        return f"Error formatting data: {e}"


def chunk_table_by_lines(table_text: str, max_chars: int, header_lines_count: int = 2):
    """Split a table string into chunks under max_chars, keeping headers in each chunk."""
    lines = table_text.splitlines()
    if not lines:
        return [""]
    header = lines[:header_lines_count]
    data = lines[header_lines_count:]

    chunks = []
    current = header.copy()
    current_len = sum(len(l) + 1 for l in current)

    for line in data:
        add_len = len(line) + 1  # include newline
        if current_len + add_len > max_chars and len(current) > header_lines_count:
            chunks.append("\n".join(current))
            current = header.copy()
            current_len = sum(len(l) + 1 for l in current)
        current.append(line)
        current_len += add_len

    if current:
        chunks.append("\n".join(current))
    return chunks


def df_to_pretty_table(df):
    return build_fixed_table(df)


def _chunk_text(text, size):
    return [text[i:i + size] for i in range(0, len(text), size)]


def send_telegram_message(token: str, chat_id: str, title: str, df):
    """Send an HTML-formatted message to Telegram using <pre> for monospace table."""
    table = df_to_pretty_table(df)
    # Escape for HTML safety, but keep spacing and newlines inside <pre>
    # Title will be escaped per part

    # Telegram: 4096 char limit per message
    # We'll chunk by table lines to preserve headers/columns.
    # 200 char budget for title and tags; 3900 for table body
    chunks = chunk_table_by_lines(table, max_chars=3900)
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    for idx, chunk in enumerate(chunks, start=1):
        header = title if idx == 1 else f"{title} (part {idx})"
        part_html = f"<b>{html.escape(header)}</b>\n<pre>{html.escape(chunk)}</pre>"
        try:
            res = requests.post(url, json={"chat_id": chat_id, "text": part_html, "parse_mode": "HTML"})
            print(f"Telegram status {res.status_code} for {header}")
        except Exception as e:
            print(f"Telegram error for {header}: {e}")


def send_discord_embed(webhook_url: str, title: str, df, color: int = 0x2F80ED):
    """Send a Discord embed with a fixed-width table in a code block; splits by lines."""
    table = df_to_pretty_table(df)
    # Chunk by lines but wrap each in its own code block to preserve formatting
    line_chunks = chunk_table_by_lines(table, max_chars=4000)
    for idx, chunk in enumerate(line_chunks, start=1):
        embed_title = title if idx == 1 else f"{title} (part {idx})"
        description = f"```\n{chunk}\n```"
        payload = {
            "embeds": [
                {
                    "title": embed_title,
                    "description": description,
                    "color": color,
                }
            ]
        }
        try:
            res = requests.post(webhook_url, json=payload)
            print(f"Discord status {res.status_code} for {embed_title}")
        except Exception as e:
            print(f"Discord error for {embed_title}: {e}")

# --- End notification helpers ---

# Notifications: send to Telegram and Discord

TOKEN='7449783431:AAHqe61k6R14Z_YismA2VEJYeXsACZbpgYg'
#test chat id
# chat_id="-4287405834"
# Original chat id
chat_id="-1002199303920"
# discord webhook
discord_webhook_url = "https://discord.com/api/webhooks/1407828506091716689/IxpesBlfXurl0PcvQKwkvrikp67ZHqe0K2WWWwUFsmY5pXpvnADd3_KTv74wBJ3Hr5n_"

notifications = [
    ("Daily chart ENTRY: TSI Screener", filtered_stock_list),
    ("Weekly chart ENTRY: TSI Screener", weekly_tsi_entry_stock_list_filtered),
    ("Daily chart ENTRY: Indices Only - TSI Screener", indices_entry_stock_list_filtered),
    ("Daily chart EXIT: TSI Screener", exit_filtered_stock_list),
]

for title, df in notifications:
    send_telegram_message(TOKEN, chat_id, title, df)
    send_discord_embed(discord_webhook_url, title, df)


# done