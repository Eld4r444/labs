from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import (
    QComboBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QListWidget,
    QListWidgetItem,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

DONE_ROLE = Qt.ItemDataRole.UserRole
PRIORITY_ROLE = Qt.ItemDataRole.UserRole + 1
PRIORITY_COLORS = {"Важный": "#e08a00", "Срочный": "#d93025"}
DONE_COLOR = "#8a8a8a"


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.connect_signals()
        self.update_counter()
        self.statusBar().showMessage("Готово к работе")

    def init_ui(self):
        self.resize(560, 420)

        self.title_label = QLabel("Новая задача")
        self.task_input = QLineEdit()
        self.task_input.setPlaceholderText("Название задачи")
        self.priority_box = QComboBox()
        self.priority_box.addItems(["Обычный", "Важный", "Срочный"])
        self.add_button = QPushButton("Добавить")
        self.task_list = QListWidget()
        self.done_button = QPushButton("Выполнено")
        self.delete_button = QPushButton("Удалить")
        self.delete_done_button = QPushButton("Удалить выполненные")
        self.clear_button = QPushButton("Очистить всё")
        self.counter_label = QLabel()

        input_layout = QHBoxLayout()
        input_layout.addWidget(self.task_input)
        input_layout.addWidget(self.priority_box)
        input_layout.addWidget(self.add_button)

        buttons_layout = QHBoxLayout()
        buttons_layout.addWidget(self.done_button)
        buttons_layout.addWidget(self.delete_button)
        buttons_layout.addWidget(self.delete_done_button)
        buttons_layout.addWidget(self.clear_button)

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.title_label)
        main_layout.addLayout(input_layout)
        main_layout.addWidget(self.task_list)
        main_layout.addLayout(buttons_layout)
        main_layout.addWidget(self.counter_label)

        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

    def connect_signals(self):
        self.add_button.clicked.connect(self.add_task)
        self.task_input.returnPressed.connect(self.add_task)
        self.done_button.clicked.connect(self.toggle_done)
        self.delete_button.clicked.connect(self.delete_task)
        self.delete_done_button.clicked.connect(self.delete_done_tasks)
        self.clear_button.clicked.connect(self.clear_tasks)

    def add_task(self):
        text = self.task_input.text().strip()
        if not text:
            QMessageBox.warning(self, "Ошибка", "Введите название задачи")
            return
        priority = self.priority_box.currentText()
        item = QListWidgetItem(f"[{priority}] {text}")
        item.setData(DONE_ROLE, False)
        item.setData(PRIORITY_ROLE, priority)
        self.paint_item(item)
        self.task_list.addItem(item)
        self.task_input.clear()
        self.update_counter()
        self.statusBar().showMessage(f"Добавлена задача: {text}")

    def toggle_done(self):
        item = self.task_list.currentItem()
        if item is None:
            QMessageBox.warning(self, "Ошибка", "Выберите задачу")
            return
        done = not item.data(DONE_ROLE)
        item.setData(DONE_ROLE, done)
        self.paint_item(item)
        self.update_counter()
        if done:
            self.statusBar().showMessage("Задача отмечена как выполненная")
        else:
            self.statusBar().showMessage("Отметка о выполнении снята")

    def paint_item(self, item):
        done = item.data(DONE_ROLE)
        font = item.font()
        font.setStrikeOut(done)
        item.setFont(font)
        color = DONE_COLOR if done else PRIORITY_COLORS.get(item.data(PRIORITY_ROLE))
        item.setData(Qt.ItemDataRole.ForegroundRole, QColor(color) if color else None)

    def delete_task(self):
        row = self.task_list.currentRow()
        if row < 0:
            QMessageBox.warning(self, "Ошибка", "Выберите задачу для удаления")
            return
        task = self.task_list.item(row).text()
        answer = QMessageBox.question(self, "Удаление", f"Удалить задачу «{task}»?")
        if answer == QMessageBox.StandardButton.Yes:
            self.task_list.takeItem(row)
            self.update_counter()
            self.statusBar().showMessage("Задача удалена")

    def delete_done_tasks(self):
        done_rows = [
            row
            for row in range(self.task_list.count())
            if self.task_list.item(row).data(DONE_ROLE)
        ]
        if not done_rows:
            QMessageBox.information(self, "Удаление", "Выполненных задач нет")
            return
        for row in reversed(done_rows):
            self.task_list.takeItem(row)
        self.update_counter()
        self.statusBar().showMessage(f"Удалено выполненных задач: {len(done_rows)}")

    def clear_tasks(self):
        if self.task_list.count() == 0:
            QMessageBox.information(self, "Очистка", "Список задач уже пуст")
            return
        answer = QMessageBox.question(self, "Очистка", "Удалить все задачи?")
        if answer == QMessageBox.StandardButton.Yes:
            self.task_list.clear()
            self.update_counter()
            self.statusBar().showMessage("Список задач очищен")

    def count_done(self):
        return sum(
            1
            for row in range(self.task_list.count())
            if self.task_list.item(row).data(DONE_ROLE)
        )

    def update_counter(self):
        count = self.task_list.count()
        done = self.count_done()
        self.counter_label.setText(f"Количество задач: {count} (выполнено: {done})")
        self.setWindowTitle(f"Менеджер задач — задач: {count}")
