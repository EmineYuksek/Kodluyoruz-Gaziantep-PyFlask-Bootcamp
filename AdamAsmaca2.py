
#istenilen sonucu vermeyen hatalar içermektedir :)

import random


HANGMAN = [
    '________',
    '|       |',
    '|       O',
    '|       |',
    '|      /|\ ',
    '|       |',
    '|      / \ '
]

WORDS = [
    'kasa', 'bilgisayar', 'ekran', 'monitör', 'klavye' 
]

class Hangman():

    def __init__(self, word_to_guess):
        self.failed_attempts = 0
        self.word_to_guess = word_to_guess
        self.game_progress = list('_' * len(self.word_to_guess))
    

    
    #harf bulma fonksiyonu
    def find_indexes(self, letter):
        
        return [i for i, char in enumerate(self.word_to_guess) if letter == char]

    def is_invalid_letter(self, input_):
       
        return input_.isdigit() or (input_.isalpha() and len(input_) > 1)

    def print_game_status(self):
     
        print('\n')
        print('\n'.join(HANGMAN[:self.failed_attempts]))
        print('\n')
        print(' '.join(self.game_progress))

    def update_progress(self, letter, indexes):
       
        for index in indexes:
            self.game_progress[index] = letter

    def get_user_input(self):
        user_input = input('\n Lütfen bir harf girin: ')
        return user_input

    def play(self):
        
        while self.failed_attempts < len(HANGMAN):
            self.print_game_status()
            user_input = self.get_user_input()

            if self.find_indexes(user_input):   #fonksiyon ifle kontrol edildi

                return self.all_guess() #fonksiyon çağrıldı
                

            if self.is_invalid_letter(user_input):
                print('--!!Girdiğiniz değer bir harf değil! Lütfen Bir harf değeri giriniz.--')
                continue
            # (harfin önceden tahmin edilip edilmediğini kontrol et)
            if user_input in self.game_progress:
                print('---Bu harfi zaten tahmin ettiniz:) Başka bir harf tahmin edin.---')
                continue


            if user_input in self.word_to_guess:
                indexes = self.find_indexes(user_input)
                self.update_progress(user_input, indexes)
                #(Kelimede bulunacak harf kalmadıysa)
                if self.game_progress.count('_') == 0:
                    print('\n KAZANDINIZ TEBRİKLER!')
                    print('Kelime: {0}'.format(self.word_to_guess))
                    quit()
            else:
                self.failed_attempts += 1
        print("\n KAYBETTİNİZ!")
        
        return self.again_play()



    def all_guess(self):

        answer = input("Kelimenin tamamini tahmin etmek istiyor musunuz? [evet ise 'Y' veya hayır ise 'N'] : ")

        if answer.upper() == 'Y':
            forecast = input("Kelimenin tamamini tahmin edebilirsiniz : ")
            if forecast == self.word_to_guess:
                print("Tebrikler bildiniz...")
                return self.again_play()
            else:

                print("Yanlis tahmin ettiniz.Harf Tahmin Ediniz")
                
                return hangman.play()


        else:
            print("harf tahminine devam ediniz...")
            return hangman.play()   
           







    
    #tekrar oynamak veya oynamamak istediğini sorma
    def again_play(self):

        AgainPlay=input("Oyun Bitti! Tekrar Oynamak İster misiniz? [evet ise 'Y' veya hayır ise 'N'] :  ")

        if AgainPlay.upper()=='Y':
            return hangman.play()

        else:
            print("Görüşürüz! Allaha emanet ol:)")
            quit()

        

if __name__ == '__main__':
    word_to_guess = random.choice(WORDS)
    hangman = Hangman(word_to_guess)
    hangman.play()

