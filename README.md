# OB04. Принципы SOLID
1. **Структура проекта:**
   - **Модуль `classes`**:
     - Определяет базовые сущности игры:
       - **Абстрактный класс `Weapon`**: задаёт общий интерфейс для всех видов оружия (метод `attack()`).
       - Конкретные реализации оружия (`Sword`, `Bow`, `MagicStaff`) расширяют абстрактный класс `Weapon`, предоставляя свои уникальные атаки.
       - **Класс `Fighter`**: представляет игрока, который может выбирать оружие (метод `equip_weapon()`) и атаковать с его помощью (метод `attack()`).
       - **Класс `Monster`**: представляет монстра с функцией получения урона (`take_damage()`).
   - **Модуль `main`**:
     - Использует классы для создания игрового процесса: создаёт игрока, монстров, экипирует оружие и выполняет атаки.

2. **Принцип открытости/закрытости:**
   - **Открытость для расширения**: 
     - Легко добавить новое оружие, создавая новый класс, наследующий `Weapon`, и реализующий метод `attack()`.
     - Никакие изменения в существующих классах (`Fighter`, `Monster` или уже существующем оружии) не требуются.
   - **Закрытость для изменений**: 
     - Логика игрока (`Fighter`) и взаимодействия с оружием полностью изолирована от конкретных реализаций оружия.
     - Система остаётся устойчивой к изменениям, и добавление нового оружия не затрагивает уже работающий код.

3. **Пример расширения:**
   Чтобы добавить, например, новый класс оружия `Axe`, достаточно:
   ```python
   class Axe(Weapon):
       def attack(self):
           return "Топор: сокрушительный удар!"
   ```
   После этого игрок сможет выбирать и использовать это оружие без изменений в других частях системы.

4. **Результат:**
   Код организован таким образом, что добавление нового функционала требует минимальных изменений и только в тех местах, где это действительно необходимо (расширение через наследование). Это упрощает сопровождение и масштабирование проекта.