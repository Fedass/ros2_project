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

## Запуск симуляции с turtlebot 3
1. Создал рабочее пространство для TurtleBot 3:
<pre><code>mkdir -p ~/turtlebot3_ws/src</code></pre>
<pre><code>cd ~/turtlebot3_ws/src</code></pre>
<pre><code>git clone -b humble https://github.com/ROBOTIS-GIT/turtlebot3_simulations.git</code></pre>
2. Собрал рабочее пространство:
<pre><code>cd ~/turtlebot3_ws && colcon build --symlink-install</code></pre>
3. Запустил симуляцию TurtleBot 3:
<pre><code>ros2 launch turtlebot3_gazebo myworld.launch.py</code></pre>
