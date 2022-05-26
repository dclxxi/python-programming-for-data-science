class Note(object):
    def __init__(self, contents):
        self.contents = contents

    def get_number_of_lines(self):
        return self.contents.count("\n") # 몇 줄인지 확인

    def get_number_of_characters(self):
        return len(self.contents) # 문자 수 확인

    def remove(self):
        self.contents = "삭제된 노트입니다."

    def __str__(self):
        return self.contents


class NoteBook(object):
    def __init__(self, name):
        self.name = name
        self.pages = 0
        self.notes = {} # 딕셔너리

    def add_note(self, note, page_number=0): # 디폴트 값
        if len(self.notes.keys()) < 300: # 마지막 페이지 300
            if page_number == 0:
                if self.pages < 301:
                    self.notes[self.pages] = note
                    self.pages += 1
                else:
                    for i in range(300):
                        if i not in list(self.notes.keys()): # 존재하지 않는 값 찾음
                            self.notes[self.pages] = note
            else: # 페이지 번호 직접 입력
                if page_number not in self.notes.keys():
                    self.notes[page_number] = note
                else:
                    print("해당 페이지에는 이미 노트가 존재합니다.")
        else:
            print("더 이상 노트를 추가하지 못합니다.")

    def remove_note(self, page_number):
        del self.notes[page_number]

    def get_number_of_all_lines(self):
        result = 0
        for k in self.notes.keys():
            result += self.notes[k].get_number_of_lines() # 노트마다 개행문자 세서 누적 = 모든 페이지 라인 수
        return result

    def get_number_of_all_characters(self):
        result = 0
        for k in self.notes.keys():
            result += self.notes[k].get_number_of_characters()
        return result

    def get_number_of_all_pages(self):
        return len(self.notes.keys())

    def __str__(self):
        return self.name
