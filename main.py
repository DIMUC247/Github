from flask import Flask, render_template


app = Flask(__name__)


@app.get("/")
def index():
    return render_template("index.html", title="Моя супер піцерія")


@app.get("/menu-MEGAAA menu/")
def menu():
    pizzas = [
        {"name": "хароша піцца", "price": 22, "ingredients": "ковбаса 'Пепероні', сир, соус"},
        {"name": "сама нормальна піцца", "price": 29, "ingredients": "ковбаса 'Пепероні', сир, соус"},
        {"name": "ну кароче такое се піцца", "price": 20, "ingredients": "сир 'Моцарела', соус, петрушка"},
        {"name": "сама дорога і крута піцца", "price": 30, "ingredients": "сир 'Моцарела', сир 'Чедер', сир 'Сологуні', сир 'Брі',всі типи мяса і все саме круте"}
    ]
    context = {
        "pizzas": pizzas,
        "title": "PIZZA меню"
    }
    return render_template("menu.html", **context)


if __name__ == "__main__":
    app.run(debug=True)