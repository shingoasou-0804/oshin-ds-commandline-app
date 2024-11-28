class Employee:
    def __init__(self, name: str, department: str) -> None:
        self.name = name
        self.department = department

    def calculate_pay(self):
        self.get_regular_hours()
        print(f"{self.name}の給与を計算しました")

    def report_hours(self):
        self.get_regular_hours()
        print(f"{self.name}の労働時間をレポートしました")

    def save(self):
        print(f"{self.name}を保存しました")

    def get_regular_hours(self):
        # 仕様変更前のロジック
        # print("経理部門・人事部門共通のロジック")

        # 仕様変更後のロジック
        print("経理部門の仕様変更済み")

if __name__ == "__main__":
    emp = Employee("山田", "開発")
    print("経理部門")
    emp.calculate_pay()

    print("")
    print("人事部門")
    emp.report_hours()
