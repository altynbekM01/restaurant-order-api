import enum

class OrderStatus(str, enum.Enum):
    processing = "в обработке"
    preparing = "готовится"
    delivering = "доставляется"
    completed = "завершен"
