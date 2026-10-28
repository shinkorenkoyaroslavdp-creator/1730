import project 

def main():
    try:
        project.main_window.show()
        project.app.exec()      
    except:
        ...

if __name__ == "__main__":
    main()