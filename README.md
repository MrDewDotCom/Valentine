# 💝 Valentine Gift Page

A one-page Valentine surprise:

1. A 3D gift box spins on a dark background.
2. Tap it and the lid pops off and flies away.
3. Scroll, swipe up or pinch to move into the box. Inside, 3D roses lie piled on a handwritten note: **"Will you be my Valentine?"**
4. Point at an answer and a pencil circle is drawn around it. Clicking **No** makes "No" shrink and "Yes" grow.
5. **Yes** shows a celebration, then a slideshow of your own photos.

Music and sound effects are made by the code itself, so there are no audio files to download (you can add your own songs if you like). There's a 🔊 button to mute.

---

## 📁 Files

```
lover/
├── index.html      ← the whole website (design, animation, sound, settings)
├── photos/         ← put your pictures here
│   ├── photo1.jpg
│   ├── photo2.jpg
│   └── photo3.jpg
├── sounds/         ← (optional) create this folder for your own mp3 files
└── README.md       ← this guide
```

## ▶️ How to open it

Double-click `index.html` to open it in your browser. To see it on a phone or share it, put it online with [GitHub Pages](#-put-it-online-github-pages) (below).

---

## ✏️ Customizing: everything is in one place

Open `index.html` in any text editor (VS Code, Notepad…). Search (**Ctrl + F**) for:

```
SETTINGS: change everything here
```

It's near the start of the `<script>` part (around **line 525**). Everything below is inside the `CONFIG = { … }` block there. You only change the values on the right side, and you keep the quotes `' '`.

### 1. Words / messages → `text:`

| Setting | Where it shows |
|---|---|
| `tapHint` | Above the closed gift ("tap it 💌") |
| `insideHint` | After the gift opens ("Something's inside…") |
| `question` | On the note. `<br>` starts a new line |
| `yes` / `no` | The two answers |
| `noReplies` | What "No" turns into each time it's clicked |
| `signature` | Small text at the bottom of the note |
| `yesTitle` / `yesSubtitle` | Big message after clicking Yes |

Example:
```js
question: 'Will you go out<br>with me, Mint?',
```

> If your text has an apostrophe (like *Valentine's*), wrap it in double quotes: `"Valentine's Day"`.

### 2. Photos → `photos:`

1. Copy your pictures into the **`photos`** folder (`.jpg`, `.png` or `.webp`). Square or portrait photos look best.
2. List them in `photos:`, one line each, with a caption:

```js
photos: [
  { src: 'photos/first-date.jpg', caption: 'Our first date 💕' },
  { src: 'photos/beach.jpg',      caption: 'Hua Hin, 2025 🌊' },
  { src: 'photos/us.png',         caption: 'Forever ✨' },
],
```

- You can list as many photos as you want, and they play in the order listed.
- `slideSeconds: 4` sets how long each photo stays on screen.
- `photosDelay: 2.5` sets how many seconds after "Yes" the photos appear.
- To have no slideshow, use `photos: [],`
- If a photo shows *"📷 Photo not found"*, the file name in `src` doesn't match the file. Check the spelling, the upper/lower case, and the extension (`.jpg` vs `.jpeg`).
- The three included photos are placeholders. Replace them, or delete them and list your own.

### 3. Sound → `sound:`

| Setting | What it does |
|---|---|
| `startMuted: true` | The page starts silent, and the 🔊 button turns sound on |
| `musicVolume` | Background music volume, `0` (silent) to `1` (full) |
| `effectsVolume` | Sound-effects volume, `0` to `1` |

**Use your own song or sound effects:** make a folder called `sounds`, put your mp3 files in it, and write the file names in `files:`:

```js
files: {
  music:  'sounds/our-song.mp3',   // background song (loops)
  open:   'sounds/pop.mp3',        // gift opens
  reveal: '',                      // reaching the note   ('' = built-in sound)
  hover:  '',                      // pointing at Yes / No
  no:     'sounds/sad.mp3',        // clicking No
  yes:    'sounds/yay.mp3',        // clicking Yes
},
```

Any setting left as `''` keeps the built-in sound.

> Browsers don't allow sound until the visitor taps or clicks something, so the page is silent until the gift is clicked. That's normal.
>
> The 🔊 button remembers its setting in that browser. If you're testing `startMuted` and nothing changes, click 🔊 once, or open the page in a private window.

### 4. Rose colours → `roseColors:`

Each line is one rose colour: `[outer petals, middle petals, dark centre]`. Use any colour codes, for example from [htmlcolorcodes.com](https://htmlcolorcodes.com):

```js
roseColors: [
  ['#ffffff', '#f3e6ea', '#d9b8c2'],   // white roses
  ['#e8335f', '#c9244f', '#8f1234'],   // red roses
],
```

---

## 🛠️ Going further (optional, for when you're comfortable with code)

Search `index.html` for these words:

| What | Search for | Notes |
|---|---|---|
| Background colours | `--bg1:` (top of the file) | `--bg1`, `--bg2` = the pink/purple glow after opening |
| Where the roses lie | `const pile = [` | Each rose is `[x, y, size, height]`. They're automatically kept inside the box |
| The built-in music melody | `const chords =` | Notes are MIDI numbers (60 = middle C). `order` = chord order, `tops` = melody notes. Change `const beat = 60 / 72` (72 = beats per minute) to change the speed |
| How fast scrolling zooms in | `0.0011` | Bigger number = faster zoom |
| How the lid flies away | `@keyframes lidAway` | The end position and spin of the lid |
| Celebration confetti | `const pieces = [` | The emojis that fall after "Yes" |

---

## 🌐 Put it online (GitHub Pages)

1. Push your changes:
   ```bash
   git add .
   git commit -m "My photos and message"
   git push
   ```
2. On GitHub, open the repo → **Settings** → **Pages**.
3. Under *Branch*, choose **main** and **/ (root)**, then **Save**.
4. After about a minute you'll get a link like
   `https://mrdewdotcom.github.io/Valentine/`. Send it to your Valentine 💌

> Photo names on GitHub Pages are case-sensitive: `Photo1.JPG` ≠ `photo1.jpg`.
