"""
pybot.py — PyBot Chatbot with On-Screen Clickable Keyboard
Run: python pybot.py
No external libraries needed — only Python built-in tkinter!
"""

import tkinter as tk
from tkinter import scrolledtext, font
import random
import time


# ══════════════════════════════════════════════════
#   CHATBOT BRAIN
# ══════════════════════════════════════════════════

GREETINGS      = ["hello", "hi", "hey", "hiya", "howdy", "sup", "whats up", "what's up", "yo"]
FAREWELLS      = ["bye", "goodbye", "see you", "see ya", "later", "take care", "exit", "quit", "farewell"]
HOW_ARE_YOU    = ["how are you", "how are u", "how r you", "how do you do", "how's it going",
                  "hows it going", "how you doing", "you good", "how you doin"]
NAME_QUESTIONS = ["what is your name", "what's your name", "whats your name",
                  "who are you", "tell me your name", "your name"]
THANKS         = ["thanks", "thank you", "thank u", "thx", "ty", "cheers", "appreciate"]
HELP_WORDS     = ["help", "what can you do", "commands", "options", "features", "menu"]
AGE_QUESTIONS  = ["how old are you", "what is your age", "your age", "age"]
JOKE_REQUESTS  = ["tell me a joke", "joke", "funny", "make me laugh", "humor", "laugh"]
TIME_QUESTIONS = ["what time is it", "what's the time", "current time", "time now", "time"]
SAD_WORDS      = ["sad", "unhappy", "depressed", "lonely", "bored", "tired", "stressed", "upset"]
FEEL_GOOD      = ["nice", "cool", "awesome", "great", "wow", "amazing", "wonderful", "love it"]
COMPLIMENTS    = ["you are great", "you're great", "good bot", "you're smart", "you are smart",
                  "you're amazing", "you are amazing", "you're clever", "well done"]
WEATHER_WORDS  = ["weather", "rain", "sunny", "forecast", "temperature", "hot", "cold"]
CREATOR_WORDS  = ["who made you", "who created you", "your creator", "who built you", "developer"]
LOVE_WORDS     = ["i love you", "love you", "i like you"]
ABOUT_WORDS    = ["what are you", "are you human", "are you a robot", "are you real", "are you ai"]

GREETING_REPLIES   = ["Hi there! 😊 Great to see you!", "Hello! What's on your mind today?",
                       "Hey hey! 👋 So glad you stopped by!", "Hi! You just made my day brighter! ✨"]
FAREWELL_REPLIES   = ["Goodbye! It was wonderful chatting! 👋", "See you later! Come back anytime! 🌟",
                       "Bye! Stay awesome out there! 😊", "Farewell, friend! Until next time! 🚀"]
HOW_ARE_YOU_REPLIES= ["I'm doing fantastic, thanks! 😄 How about you?",
                       "Running at 100%! Every line of code is happy! 💡",
                       "Feeling great! Chatting with you is the highlight of my day! ☀️"]
THANKS_REPLIES     = ["You're so welcome! 😊", "Anytime! That's what I'm here for!",
                       "No problem at all! Happy to help! 🙌", "My pleasure! You're very kind! 💛"]
JOKES = [
    "Why don't scientists trust atoms?\nBecause they make up everything! 😂",
    "Why did the scarecrow win an award?\nBecause he was outstanding in his field! 🌾",
    "Why do programmers prefer dark mode?\nBecause light attracts bugs! 🐛",
    "What do you call a fish without eyes?\nA fsh! 🐟",
    "Why was the math book sad?\nBecause it had too many problems! 📚",
]
SAD_REPLIES        = ["Aww, I'm sorry to hear that 💛 I'm here for you!",
                       "Sending you virtual hugs! 🤗 Things will get better!",
                       "I'm here with you! Type 'joke' for a laugh! 😊"]
FEEL_GOOD_REPLIES  = ["That's so good to hear! 😄", "Love the positive energy! ✨",
                       "Awesome! You're making me happy too! 🎉"]
COMPLIMENT_REPLIES = ["Aww, you just made me blush (in binary)! 😊💛",
                       "You're too kind! I'm just a humble bot! 🤖",
                       "Thank you! You're my favourite human today! 🌟"]
UNKNOWN_REPLIES    = ["Hmm, that's a new one! 🤔 Try typing 'help'.",
                       "I'm still learning! Try asking something else 😅",
                       "I didn't catch that — type 'help' to see what I know!"]

HELP_TEXT = (
    "📋  Here's what I understand:\n\n"
    "  👋  hello / hi / hey\n"
    "  ❓  how are you\n"
    "  🏷️   what is your name\n"
    "  🎂  how old are you\n"
    "  😂  tell me a joke\n"
    "  ⏰  what time is it\n"
    "  😢  i am sad / i am bored\n"
    "  🙏  thanks / thank you\n"
    "  💛  i love you\n"
    "  🚪  bye / goodbye\n\n"
    "  Use the keyboard or buttons below! 😊"
)


def normalize(text):
    return text.lower().strip()

def contains(text, keywords):
    for word in keywords:
        if word in text:
            return True
    return False

def get_response(user_input):
    text = normalize(user_input)
    if not text:
        return "Please type something! 👂", False
    if contains(text, FAREWELLS):
        return random.choice(FAREWELL_REPLIES), True
    elif contains(text, GREETINGS):
        return random.choice(GREETING_REPLIES), False
    elif contains(text, HOW_ARE_YOU):
        return random.choice(HOW_ARE_YOU_REPLIES), False
    elif contains(text, NAME_QUESTIONS):
        return "I'm PyBot 🤖 — your friendly Python chatbot!", False
    elif contains(text, CREATOR_WORDS):
        return "I was built with 💛 using pure Python — if-elif logic, functions & loops!", False
    elif contains(text, ABOUT_WORDS):
        return "I'm PyBot — a rule-based chatbot built in Python! Friendly but not human 🤖", False
    elif contains(text, AGE_QUESTIONS):
        return "I was born the moment you ran this script — brand new! 🐣", False
    elif contains(text, JOKE_REQUESTS):
        return random.choice(JOKES), False
    elif contains(text, TIME_QUESTIONS):
        return f"The current time is  {time.strftime('%I:%M %p')}  ⏰", False
    elif contains(text, WEATHER_WORDS):
        return "I can't check real weather, but I hope it's sunny! ☀️", False
    elif contains(text, SAD_WORDS):
        return random.choice(SAD_REPLIES), False
    elif contains(text, FEEL_GOOD):
        return random.choice(FEEL_GOOD_REPLIES), False
    elif contains(text, COMPLIMENTS):
        return random.choice(COMPLIMENT_REPLIES), False
    elif contains(text, LOVE_WORDS):
        return "Aww, I love you too! 💛 You're the best user I've ever had!", False
    elif contains(text, THANKS):
        return random.choice(THANKS_REPLIES), False
    elif contains(text, HELP_WORDS):
        return HELP_TEXT, False
    else:
        return random.choice(UNKNOWN_REPLIES), False


# ══════════════════════════════════════════════════
#   COLOURS
# ══════════════════════════════════════════════════

BG         = "#0f1117"
SURFACE    = "#1a1d27"
CARD       = "#21263a"
BORDER     = "#2e3348"
ACCENT     = "#00e5a0"
ACCENT2    = "#00aaff"
TEXT       = "#e4e8f0"
MUTED      = "#6b7280"
BOT_BG     = "#1e2535"
USER_BG    = "#005f45"
INPUT_BG   = "#161922"
TIMESTAMP  = "#4a5568"
DANGER     = "#ff6b6b"
KEY_BG     = "#21263a"
KEY_FG     = "#e4e8f0"
KEY_HOVER  = "#00e5a0"
KEY_HOVER_FG = "#0f1117"


# ══════════════════════════════════════════════════
#   ON-SCREEN KEYBOARD LAYOUT
# ══════════════════════════════════════════════════

KEYBOARD_ROWS = [
    ["1","2","3","4","5","6","7","8","9","0","⌫"],
    ["q","w","e","r","t","y","u","i","o","p"],
    ["a","s","d","f","g","h","j","k","l","'"],
    ["z","x","c","v","b","n","m",",","."," "],
    ["SEND ✉"],
]

# Quick phrase shortcuts
QUICK_PHRASES = [
    "Hello!",
    "How are you?",
    "Tell me a joke",
    "What time is it?",
    "What is your name?",
    "I love you",
    "Help",
    "Bye",
]


# ══════════════════════════════════════════════════
#   GUI APPLICATION
# ══════════════════════════════════════════════════

class PybotApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PyBot — Chat Buddy 🤖")
        self.root.geometry("700x850")
        self.root.minsize(640, 750)
        self.root.configure(bg=BG)
        self.root.resizable(True, True)

        self.caps = False   # caps lock state

        self._build_header()
        self._build_chat_area()
        self._build_quick_phrases()
        self._build_display_input()
        self._build_keyboard()
        self._welcome()

    # ── HEADER ───────────────────────────────────

    def _build_header(self):
        hdr = tk.Frame(self.root, bg=SURFACE, pady=10)
        hdr.pack(fill="x")

        tk.Label(hdr, text="🤖", font=("Segoe UI Emoji", 26),
                 bg=ACCENT, width=2).pack(side="left", padx=(16, 10))

        info = tk.Frame(hdr, bg=SURFACE)
        info.pack(side="left")
        tk.Label(info, text="PyBot", font=("Segoe UI", 15, "bold"),
                 bg=SURFACE, fg=TEXT).pack(anchor="w")

        row = tk.Frame(info, bg=SURFACE)
        row.pack(anchor="w")
        self.dot = tk.Label(row, text="●", font=("Segoe UI", 9), bg=SURFACE, fg=ACCENT)
        self.dot.pack(side="left")
        self.status = tk.Label(row, text="  Online", font=("Segoe UI", 9),
                                bg=SURFACE, fg=MUTED)
        self.status.pack(side="left")

        tk.Button(hdr, text="🗑 Clear", font=("Segoe UI", 9),
                  bg=CARD, fg=MUTED, relief="flat", cursor="hand2",
                  activebackground=BORDER, activeforeground=TEXT,
                  command=self._clear_chat, padx=10, pady=5).pack(side="right", padx=16)

        tk.Frame(self.root, bg=BORDER, height=1).pack(fill="x")

    # ── CHAT DISPLAY ─────────────────────────────

    def _build_chat_area(self):
        self.chat_box = scrolledtext.ScrolledText(
            self.root, state="disabled", wrap="word",
            font=("Segoe UI", 11), bg=BG, fg=TEXT,
            relief="flat", bd=0, padx=16, pady=12,
            cursor="arrow", spacing3=4, height=10
        )
        self.chat_box.pack(fill="both", expand=True)

        self.chat_box.tag_configure("bot_name",  foreground=ACCENT,  font=("Segoe UI", 9, "bold"))
        self.chat_box.tag_configure("bot_text",  foreground=TEXT,    font=("Segoe UI", 11),
                                    background=BOT_BG, lmargin1=12, lmargin2=12,
                                    rmargin=100, spacing1=3, spacing3=3)
        self.chat_box.tag_configure("user_name", foreground=ACCENT2, font=("Segoe UI", 9, "bold"), justify="right")
        self.chat_box.tag_configure("user_text", foreground="#ffffff", font=("Segoe UI", 11),
                                    background=USER_BG, lmargin1=100, lmargin2=100,
                                    rmargin=12, spacing1=3, spacing3=3, justify="right")
        self.chat_box.tag_configure("timestamp", foreground=TIMESTAMP, font=("Segoe UI", 8), spacing3=8)
        self.chat_box.tag_configure("typing",    foreground=MUTED, font=("Segoe UI", 10, "italic"))
        self.chat_box.tag_configure("farewell",  foreground=DANGER, font=("Segoe UI", 10, "italic"),
                                    justify="center", spacing1=6, spacing3=6)

        tk.Frame(self.root, bg=BORDER, height=1).pack(fill="x")

    # ── QUICK PHRASES ─────────────────────────────

    def _build_quick_phrases(self):
        outer = tk.Frame(self.root, bg=SURFACE, pady=6)
        outer.pack(fill="x")

        tk.Label(outer, text="  Quick phrases:", font=("Segoe UI", 9),
                 bg=SURFACE, fg=MUTED).pack(side="left")

        scroll_frame = tk.Frame(outer, bg=SURFACE)
        scroll_frame.pack(side="left", fill="x", expand=True)

        for phrase in QUICK_PHRASES:
            btn = tk.Button(
                scroll_frame, text=phrase,
                font=("Segoe UI", 9),
                bg=CARD, fg=TEXT, relief="flat",
                cursor="hand2", padx=8, pady=3,
                activebackground=ACCENT, activeforeground=BG,
                command=lambda p=phrase: self._quick_send(p)
            )
            btn.pack(side="left", padx=3)
            btn.bind("<Enter>", lambda e, b=btn: b.config(bg=ACCENT, fg=BG))
            btn.bind("<Leave>", lambda e, b=btn: b.config(bg=CARD, fg=TEXT))

        tk.Frame(self.root, bg=BORDER, height=1).pack(fill="x")

    # ── MESSAGE DISPLAY INPUT ─────────────────────

    def _build_display_input(self):
        """Shows what the user is currently typing."""
        frame = tk.Frame(self.root, bg=INPUT_BG, pady=0)
        frame.pack(fill="x")

        tk.Label(frame, text=" You:", font=("Segoe UI", 10, "bold"),
                 bg=INPUT_BG, fg=ACCENT2).pack(side="left", padx=(10, 4), pady=8)

        self.input_var = tk.StringVar()
        self.input_display = tk.Label(
            frame, textvariable=self.input_var,
            font=("Segoe UI", 12), bg=INPUT_BG, fg=TEXT,
            anchor="w", width=38
        )
        self.input_display.pack(side="left", fill="x", expand=True, pady=8)

        # Blinking cursor label
        self.cursor_visible = True
        self.cursor_label = tk.Label(frame, text="▌", font=("Segoe UI", 14),
                                      bg=INPUT_BG, fg=ACCENT)
        self.cursor_label.pack(side="left", pady=8)
        self._blink_cursor()

        tk.Frame(self.root, bg=BORDER, height=1).pack(fill="x")

    def _blink_cursor(self):
        self.cursor_visible = not self.cursor_visible
        self.cursor_label.config(fg=ACCENT if self.cursor_visible else INPUT_BG)
        self.root.after(530, self._blink_cursor)

    # ── ON-SCREEN KEYBOARD ────────────────────────

    def _build_keyboard(self):
        kb_outer = tk.Frame(self.root, bg=BG, pady=6)
        kb_outer.pack(fill="x", padx=8, pady=(4, 8))

        for row_keys in KEYBOARD_ROWS:
            row_frame = tk.Frame(kb_outer, bg=BG)
            row_frame.pack(pady=3)

            for key in row_keys:
                self._make_key(row_frame, key)

    def _make_key(self, parent, key):
        # Special key widths
        if key == "SEND ✉":
            w, h, bg, fg = 28, 2, ACCENT, BG
        elif key == "⌫":
            w, h, bg, fg = 5, 2, "#3a2020", DANGER
        elif key == " ":
            w, h, bg, fg = 18, 2, CARD, TEXT
            display = "SPACE"
        else:
            w, h, bg, fg = 4, 2, KEY_BG, KEY_FG
            display = key

        display = key if key not in [" "] else "SPACE"

        btn = tk.Button(
            parent,
            text=display,
            font=("Segoe UI", 10, "bold") if key == "SEND ✉" else ("Consolas", 11),
            bg=bg, fg=fg,
            relief="flat",
            cursor="hand2",
            width=w, height=h,
            activebackground=KEY_HOVER if key != "SEND ✉" else "#00c88c",
            activeforeground=KEY_HOVER_FG,
            command=lambda k=key: self._key_press(k)
        )
        btn.pack(side="left", padx=2)

        if key not in ["SEND ✉", "⌫"]:
            btn.bind("<Enter>", lambda e, b=btn: b.config(bg=KEY_HOVER, fg=KEY_HOVER_FG))
            btn.bind("<Leave>", lambda e, b=btn, bg_=bg, fg_=fg: b.config(bg=bg_, fg=fg_))

    # ── KEY PRESS LOGIC ───────────────────────────

    def _key_press(self, key):
        if key == "⌫":
            # Backspace
            current = self.input_var.get()
            self.input_var.set(current[:-1])

        elif key == "SEND ✉":
            self._send_message()

        elif key == " ":
            self.input_var.set(self.input_var.get() + " ")

        else:
            char = key.upper() if self.caps else key
            self.input_var.set(self.input_var.get() + char)

    # ── SEND MESSAGE ──────────────────────────────

    def _quick_send(self, phrase):
        self.input_var.set(phrase)
        self._send_message()

    def _send_message(self):
        raw = self.input_var.get().strip()
        if not raw:
            return

        self.input_var.set("")
        self._append_user(raw)
        self.root.after(200, lambda: self._show_typing(raw))

    def _show_typing(self, user_msg):
        self._write("  🤖 PyBot is typing...\n", "typing")
        self._scroll()
        delay = random.randint(600, 1000)
        self.root.after(delay, lambda: self._deliver(user_msg))

    def _deliver(self, user_msg):
        self.chat_box.config(state="normal")
        self.chat_box.delete("end-2l", "end")
        self.chat_box.config(state="disabled")

        reply, should_exit = get_response(user_msg)
        self._append_bot(reply)

        if should_exit:
            self._handle_farewell()

    # ── BUBBLE RENDERING ──────────────────────────

    def _append_user(self, text):
        ts = time.strftime("%I:%M %p")
        self._write("\n", "timestamp")
        self._write("                                         You\n", "user_name")
        self._write(f"  {text}\n", "user_text")
        self._write(f"                                    {ts}\n", "timestamp")
        self._scroll()

    def _append_bot(self, text):
        ts = time.strftime("%I:%M %p")
        self._write("\n", "timestamp")
        self._write("  🤖 PyBot\n", "bot_name")
        self._write(f"  {text}\n", "bot_text")
        self._write(f"  {ts}\n", "timestamp")
        self._scroll()

    def _write(self, text, tag=None):
        self.chat_box.config(state="normal")
        if tag:
            self.chat_box.insert("end", text, tag)
        else:
            self.chat_box.insert("end", text)
        self.chat_box.config(state="disabled")

    def _scroll(self):
        self.chat_box.see("end")

    # ── FAREWELL & CLEAR ──────────────────────────

    def _handle_farewell(self):
        self._write("\n  ── Chat ended. Press 🗑 Clear to start again. ──\n", "farewell")
        self.status.config(text="  Offline", fg=DANGER)
        self.dot.config(fg=DANGER)
        self._scroll()

    def _clear_chat(self):
        self.chat_box.config(state="normal")
        self.chat_box.delete("1.0", "end")
        self.chat_box.config(state="disabled")
        self.input_var.set("")
        self.status.config(text="  Online", fg=MUTED)
        self.dot.config(fg=ACCENT)
        self._welcome()

    def _welcome(self):
        self._append_bot(
            "Hello! I'm PyBot 👋\n"
            "  Use the keyboard below to type,\n"
            "  or tap a Quick Phrase button above!\n"
            "  Type 'help' to see all my commands 😊"
        )


# ══════════════════════════════════════════════════
#   RUN
# ══════════════════════════════════════════════════

if __name__ == "__main__":
    root = tk.Tk()
    app = PybotApp(root)
    root.mainloop()
