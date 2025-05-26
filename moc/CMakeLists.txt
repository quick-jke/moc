add_library(moc INTERFACE)

add_subdirectory(core)

target_link_libraries(moc
    INTERFACE
        Core
        
)


target_include_directories(moc
    INTERFACE
        $<BUILD_INTERFACE:${PROJECT_SOURCE_DIR}>
        $<INSTALL_INTERFACE:include>
)