# Этапы выполнения работы.

## Создание квартиры
1. Сначала я запустил gazebo.
2. Потом перешел в режим building_editor и начертил 2д макет квартиры.
3. Вставил элементы Wall, Window и Door.
4. Сохранил модель в папке building_editor_models

## Загрузка квартиры в Ignition Gazebo
1. Создал в папке building_editor_models файл world.sdf, который позволяет загрузить квартиру в мир Ignition Gazebo, используя модель из файла model.sdf
2. Загрузил мир командой 
ign gazebo world.sdf 
3. В симуляции загрузил предметы мебели, пол и свет.
4. Сохранил мир через "Save world as", файл с раширением sdf (лучше выбрать тот же самый файл world.sdf), поставил "Expand include tags" и "Save Fuel model version".

## Запуск симуляции с turtlebot 4
1. Создал рабочее пространство для TurtleBot 4:
mkdir -p ~/turtlebot4_ws/src
cd ~/turtlebot4_ws/src
git clone https://github.com/turtlebot/turtlebot4.git
2. Составил рабочее пространство:
cd ~/turtlebot4_ws
colcon build --symlink-install
3. Запустил симуляцию TurtleBot 4:
ros2 launch turtlebot4_ignition_bringup turtlebot4_ignition.launch.py nav2:=true slam:=false localization:=true rviz:=true

