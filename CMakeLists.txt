cmake_minimum_required(VERSION 3.14)

project(MedagePlayer VERSION 0.1 LANGUAGES CXX)

set(CMAKE_INCLUDE_CURRENT_DIR ON)

set(CMAKE_AUTOUIC ON)
set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTORCC ON)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

find_package(QT NAMES Qt6 Qt5 REQUIRED COMPONENTS Core Quick)
find_package(Qt${QT_VERSION_MAJOR} REQUIRED COMPONENTS Core Quick)
find_package(Qt6 REQUIRED COMPONENTS QuickControls2)

set(PROJECT_SOURCES
        settings.h
        main.cpp
        qml.qrc
        settings.cpp
#        pyPlayer.py
#        mainloop.py
#        windowConnect.py
        Songs/sf.mp3
        Playlists/Library.txt
        Playlists/Queue.txt
        ITCOTD.jpg
        fileio.h
        fileio.cpp
#        SpotifyCredentials.py
#        SpotifyData.py
#        SpotifyUser.py
#        YTMCredentials.py
#        YTMUser.py
)

qt6_add_qml_module(FileIO
    URI "FileIO"
    VERSION 1.0
    OUTPUT_DIRECTORY FileIO
    SOURCES
        fileio.h
        fileio.cpp
)

if(${QT_VERSION_MAJOR} GREATER_EQUAL 6)
    qt_add_executable(MedagePlayer
        MANUAL_FINALIZATION
        ${PROJECT_SOURCES}
    )
# Define target properties for Android with Qt 6 as:
#    set_property(TARGET MedagePlayer APPEND PROPERTY QT_ANDROID_PACKAGE_SOURCE_DIR
#                 ${CMAKE_CURRENT_SOURCE_DIR}/android)
# For more information, see https://doc.qt.io/qt-6/qt-add-executable.html#target-creation
else()
    if(ANDROID)
        add_library(MedagePlayer SHARED
            ${PROJECT_SOURCES}
        )
# Define properties for Android with Qt 5 after find_package() calls as:
#    set(ANDROID_PACKAGE_SOURCE_DIR "${CMAKE_CURRENT_SOURCE_DIR}/android")
    else()
        add_executable(MedagePlayer
          ${PROJECT_SOURCES}
        )
    endif()
endif()

target_compile_definitions(MedagePlayer
  PRIVATE $<$<OR:$<CONFIG:Debug>,$<CONFIG:RelWithDebInfo>>:QT_QML_DEBUG>)
target_link_libraries(MedagePlayer
  PRIVATE Qt${QT_VERSION_MAJOR}::Core Qt${QT_VERSION_MAJOR}::Quick)
target_link_libraries(MedagePlayer PRIVATE Qt6::QuickControls2)
target_link_libraries(MedagePlayer PRIVATE Qt6::Core)

set_target_properties(MedagePlayer PROPERTIES
    MACOSX_BUNDLE_GUI_IDENTIFIER my.example.com
    MACOSX_BUNDLE_BUNDLE_VERSION ${PROJECT_VERSION}
    MACOSX_BUNDLE_SHORT_VERSION_STRING ${PROJECT_VERSION_MAJOR}.${PROJECT_VERSION_MINOR}
    MACOSX_BUNDLE TRUE
    WIN32_EXECUTABLE TRUE
)

if(QT_VERSION_MAJOR EQUAL 6)
    qt_import_qml_plugins(MedagePlayer)
    qt_finalize_executable(MedagePlayer)

endif()
