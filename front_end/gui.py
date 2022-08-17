from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from tkinter import filedialog as fd

from cv2 import FileNode_NAMED

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = Tk()

#def open_file():
    

window.geometry("643x417")
window.configure(bg = "#075E54")


canvas = Canvas(
    window,
    bg = "#075E54",
    height = 417,
    width = 643,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    1.0,
    92.0,
    643.0,
    417.0,
    fill="#FDFBFB",
    outline="")

canvas.create_text(
    18.0,
    17.0,
    anchor="nw",
    text="Face Recognition Application",
    fill="#FDFBFB",
    font=("Alata Regular", 40 * -1)
)

canvas.create_text(
    317.0,
    158.0,
    anchor="nw",
    text="Upload the video or image:",
    fill="#000000",
    font=("OverpassRoman Regular", 22 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=354.0,
    y=279.0,
    width=189.0,
    height=54.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=354.0,
    y=207.0,
    width=189.0,
    height=54.0
)

canvas.create_rectangle(
    0.0,
    92.0,
    277.0,
    417.0,
    fill="#71A29C",
    outline="")

canvas.create_text(
    18.0,
    132.0,
    anchor="nw",
    text="Click on the Browse button",
    fill="#FFFFFF",
    font=("Alata", 16 * -1)
)

canvas.create_text(
    18.0,
    154.0,
    anchor="nw",
    text="to upload a low quality",
    fill="#FFFFFF",
    font=("Alata", 16 * -1)
)

canvas.create_text(
    18.0,
    176.0,
    anchor="nw",
    text="image or video from your",
    fill="#FFFFFF",
    font=("Alata", 16 * -1)
)

canvas.create_text(
    18.0,
    198.0,
    anchor="nw",
    text="computer.",
    fill="#FFFFFF",
    font=("Alata", 16 * -1)
)

canvas.create_text(
    18.0,
    245.0,
    anchor="nw",
    text="Then click on the Generate",
    fill="#FFFFFF",
    font=("Alata", 16 * -1)
)

canvas.create_text(
    18.0,
    267.0,
    anchor="nw",
    text="button to enhance the uploaded",
    fill="#FFFFFF",
    font=("Alata", 16 * -1)
)

canvas.create_text(
    18.0,
    289.0,
    anchor="nw",
    text="file and recogonize faces from",
    fill="#FFFFFF",
    font=("Alata", 16 * -1)
)

canvas.create_text(
    18.0,
    311.0,
    anchor="nw",
    text="the enhanced file.",
    fill="#FFFFFF",
    font=("Alata", 16 * -1)
)
window.resizable(False, False)
window.mainloop()
