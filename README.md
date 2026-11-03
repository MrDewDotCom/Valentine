# 💝 Valentine Gift Page

A one-page 3D Valentine surprise. A gift box spins on a dark background, it opens with the animation you choose, and inside, 3D flowers lie on a handwritten note asking **"Will you be my Valentine?"** Pointing at an answer draws a pencil circle around it. Clicking **No** makes it shrink. Clicking **Yes** starts a celebration and then a slideshow of your photos. The music and sound effects are made by the page itself, or you can add your own song.

---

## 🚀 The easy way: `builder.html`

Double-click **`builder.html`** to open it in your browser. Everything is set up on that page with no code:

| Section | What you choose |
|---|---|
| 1. Gift box | Box colour and ribbon/bow colour (with a spinning 3D preview) |
| 2. How it opens | The 3D opening animation (see below) |
| 3. The note & messages | The question, Yes/No text, what "No" turns into, the signature and the messages after "Yes" |
| 4. Flowers in the box | Drag flowers around the bottom of the box. There are 5 types: **rose, tulip, daisy, sunflower, cherry blossom**. Click a flower to change its type, colour and size, put it on top or underneath, copy it or remove it. Quick layouts fill the box for you. Flowers can overlap: one added later rests and leans on top of the others, and never passes through them |
| 5. Behind the note | What lies on the bottom of the box around the note: **rose petals, paper hearts, confetti, crinkle paper** or nothing. Also its colour, how much there is, and the floor colour |
| 6. Music & sound | Built-in music-box melody, **your own song** (mp3), or no music. You can also turn sound effects off and set the volumes |
| 7. Photos | Choose or drop photos and add a caption to each. ◀ ▶ changes the order |

Then use the buttons at the bottom:

- **👀 Preview** lets you try it right there, on a computer-sized or phone-sized screen.
- **⬇️ Download index.html** saves **one file** with your photos and song packed inside. Send that file, or put it online (see below).
- **📂 Open a page I made** loads an `index.html` you downloaded before, so you can change it.
- **↺ Start over** goes back to the default settings.

The builder remembers your settings in that browser. Big photos and songs may not fit in its memory, so keep your downloaded `index.html` and reopen it with **📂 Open a page I made** to continue later.

### The 5 opening animations

| Mode | What happens |
|---|---|
| 🔍 **Scroll in** | Tap to open, then scroll, swipe up or pinch to move into the box yourself |
| 👆 **Tap several times** | The box hops higher with a burst of hearts on each tap. On the last tap it opens and the camera glides in. You choose the number of taps |
| ✨ **One tap** | One tap, then the lid flies off and the camera glides in by itself |
| 💗 **Press & hold** | Hold the gift while hearts fill up and it shakes harder, then it bursts open. You choose the number of seconds |
| 📦 **Unfold** | One tap, then the four walls fall open flat and the camera looks down inside |

In every mode, scrolling up (or swiping down) steps back out, and scrolling down goes back in.

---

## 📁 Files

```
lover/
├── builder.html        ← the settings page (open this to make your gift)
├── index.html          ← the gift page itself (the builder downloads a new one)
├── photos/             ← sample photos used by the default index.html
├── tools/
│   ├── builder.src.html  ← source of builder.html
│   └── make-builder.py   ← rebuilds builder.html after you edit index.html's code
└── README.md
```

---

## ✏️ Changing things by hand (optional)

Everything the builder sets is in one block near the top of `index.html`'s `<script>`. Search (**Ctrl + F**) for:

```
SETTINGS: change everything here
```

It's around **line 551**, inside `const CONFIG = { … }`. In the default `index.html` each setting has a comment explaining it.

| Setting | What it does |
|---|---|
| `box.color`, `box.ribbon` | Box and ribbon colours, for example `'#3a7bd5'` |
| `reveal.mode` | `'scroll'`, `'taps'`, `'auto'`, `'hold'` or `'unfold'` |
| `reveal.taps` / `reveal.holdSeconds` | Number of taps for "taps", seconds to hold for "hold" |
| `text.*` | All the words. `<br>` makes a new line. A long question shrinks automatically to fit the note |
| `flowers` | A list like `{ type: 'rose', color: '#e8335f', x: -60, y: -64, size: 40 }`. Types are `rose`, `tulip`, `daisy`, `sunflower` and `sakura`. `x`/`y` go from -88 to 88 (0,0 is the centre). Flowers can never poke through the box walls or through each other; later ones rest on top |
| `floor.fill` | `'petals'`, `'hearts'`, `'confetti'`, `'shred'` (crinkle paper) or `'none'`: what lies around the note |
| `floor.color`, `floor.amount` | Colour of that fill (confetti mixes its own colours), and how many pieces (0 – 200) |
| `floor.base` | Colour of the box floor itself; `''` = a darker shade of the box colour |
| `photos` | `{ src: 'photos/me.jpg', caption: '…' }`. File names are case-sensitive online |
| `slideSeconds`, `photosDelay` | Slideshow timing |
| `sound.music` | `'builtin'`, `'none'`, or a file such as `'sounds/our-song.mp3'` |
| `sound.effects` | `false` turns off the pop, chime and pencil sounds |
| `sound.files.open / reveal / hover / no / yes` | Your own mp3 for any one sound effect (`''` keeps the built-in sound) |

> Pages downloaded from the builder have the same block, without the comments, and photos and songs are stored as long `data:` text. It's easier to change those pages with **📂 Open a page I made** in the builder.

### Going further (code)

| What | Search `index.html` for |
|---|---|
| Background glow colours | `--bg1:` |
| How each flower type is built in 3D | `const FLOWERS = {` |
| The built-in melody | `const chords =` (60 = middle C; `const beat = 60 / 72` sets the speed, 72 beats per minute) |
| Scroll zoom speed | `0.0011` |
| How the lid flies away | `@keyframes lidAway` |
| Confetti emojis after "Yes" | `const pieces = [` |

If you change the **code** of `index.html` (not just the settings), run this so the builder uses your new version:

```bash
python tools/make-builder.py
```

---

## 🌐 Put it online (GitHub Pages)

1. Put the `index.html` you downloaded from the builder into this folder, replacing the old one.
2. Push:
   ```bash
   git add .
   git commit -m "My Valentine gift"
   git push
   ```
3. On GitHub, open the repo → **Settings** → **Pages** → Branch **main**, **/ (root)** → **Save**.
4. After about a minute your link is ready: `https://mrdewdotcom.github.io/Valentine/` 💌

> `builder.html` will also be online at `…/Valentine/builder.html`. If you don't want anyone to find it, keep it only on your computer (remove it from git with `git rm --cached builder.html`).
>
> Browsers only allow sound after the first tap or click, so the music starts when the gift is opened.
