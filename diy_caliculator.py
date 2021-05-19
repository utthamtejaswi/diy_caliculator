import pygame
import pygame.font

pygame.init()
font = pygame.font.Font(None, 36)
screen = pygame.display.set_mode((800,800))
pygame.display.set_caption("caliculator")
done = False
count=0
class stats():
        def __init__(self):
                self.index_dict={(0,0):(100,100), (0,1):(300,100), (0,2):(500,100), (0,3):(700,100),
                                 (1,0):(100,300), (1,1):(300,300), (1,2):(500,300), (1,3):(700,300),
                                 (2,0):(100,500), (2,1):(300,500), (2,2):(500,500), (2,3):(700,500),
                                 (3,0):(100,700), (3,1):(300,700), (3,2):(500,700), (3,3):(700,700)}
                                                                                           
                self.box_dict={(0,0):(1)  , (0,1):(2)  , (0,2):(3)   , (0,3):("+"),
                               (1,0):(4)  , (1,1):(5)  , (1,2):(6)   , (1,3):("-"),
                               (2,0):(7)  , (2,1):(8)  , (2,2):(9)   , (2,3):("/"),
                               (3,0):(00) , (3,1):(0)  , (3,2):("=") , (3,3):("*")}
                               
        def return_column(self,pos):
                self.pos=pos
                if(self.pos[0]<=200):
                        return(0)
                if(self.pos[0]<=400):
                        return(1)
                if(self.pos[0]<=600):
                        return(2)
                if(self.pos[0]<=800):
                        return(3)

        def return_row(self,pos):
                self.pos=pos
                if(self.pos[1]<=200):
                        return(0)
                if(self.pos[1]<=400):
                        return(1)
                if (self.pos[1]<=600):
                        return(2)
                if(self.pos[1]<=800):
                        return(3)

                
        def lines(self):
                pygame.draw.line(screen, (255,255,255), (200,0), (200,800),5)
                pygame.draw.line(screen, (255,255,255), (400,0), (400,800),5)
                pygame.draw.line(screen, (255,255,255), (600,0), (600,800),5)
                pygame.draw.line(screen, (255,255,255), (0,200), (800,200),5)
                pygame.draw.line(screen, (255,255,255), (0,400), (800,400),5)
                pygame.draw.line(screen, (255,255,255), (0,600), (800,600),5)

        def text(self):
                text1=font.render("1", 2, (255, 255, 255))
                text_box1 = ((100,100))
                screen.blit(text1,text_box1)

                text2=font.render("2", 2, (255, 255, 255))
                text_box2 = ((300,100))
                screen.blit(text2,text_box2)

                text3=font.render("3", 2, (255, 255, 255))
                text_box3 = ((500,100))
                screen.blit(text3,text_box3)

                textplus=font.render("+", 2, (255, 255, 255))
                text_box_plus=((700,100))
                screen.blit(textplus,text_box_plus)

                text4=font.render("4", 2, (255, 255, 255))
                text_box4 = ((100,300))
                screen.blit(text4,text_box4)

                text5=font.render("5", 2, (255, 255, 255))
                text_box5 = ((300,300))
                screen.blit(text5,text_box5)

                text6=font.render("6", 2, (255, 255, 255))
                text_box6 = ((500,300))
                screen.blit(text6,text_box6)

                textminus=font.render("-", 2, (255, 255, 255))
                text_box_minus = ((700,300))
                screen.blit(textminus,text_box_minus)

                text7=font.render("7", 2, (255, 255, 255))
                text_box7 = ((100,500))
                screen.blit(text7,text_box7)

                text8=font.render("8", 2, (255, 255, 255))
                text_box8 = ((300,500))
                screen.blit(text8,text_box8)

                text9=font.render("9", 2, (255, 255, 255))
                text_box9 = ((500,500))
                screen.blit(text9,text_box9)

                textdivide=font.render("/", 2, (255, 255, 255))
                text_box_divide = ((700,500))
                screen.blit(textdivide,text_box_divide)
                
                text00=font.render("0", 2, (255, 255, 255))
                text_box00 = ((100,700))
                screen.blit(text00,text_box00)

                text0=font.render("0", 2, (255, 255, 255))
                text_box0 = ((300,700))
                screen.blit(text0,text_box0)

                text_equal=font.render("=", 2, (255, 255, 255))
                text_box_equal = ((500,700))
                screen.blit(text_equal,text_box_equal)

                textmultiply=font.render("*", 2, (255, 255, 255))
                text_box_multiply = ((700,700))
                screen.blit(textmultiply,text_box_multiply)

        def to_do(self,number1,number2,operation):
                self.number1=number1
                self.number2=number2
                self.operation=operation
                if(self.operation=="+"):
                        return self.number1+self.number2
                if(self.operation=="-"):
                        return self.number1-self.number2
                if(self.operation=="/"):
                        return self.number1/self.number2
                if(self.operation=="*"):
                        return self.number1*self.number2
                if(self.operation=="="):
                        return "error operation entered is wrong"


obj1=stats()
num_list=[0]
num_string=""
count=0
while not done:
        obj1.lines()
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        quit()
                        exit()
                                
                if event.type == pygame.MOUSEBUTTONDOWN:
                        pos =list(pygame.mouse.get_pos())
                        pos1=75
                        column=obj1.return_column(pos)
                        row=obj1.return_row(pos)
                        box=obj1.index_dict[(row,column)]
                        box_num=obj1.box_dict[(row,column)]
                        if (box_num!= "=") and (box_num!= "+") and (box_num!= "-") and (box_num!= "/") and (box_num!= "*"): 
                                num_list.append(box_num)
                        elif (box_num == "+") or (box_num == "-") or (box_num == "/") or (box_num == "*"): 
                                operation=box_num
                                print(operation)
                                num_list=[0]
                                num_string=""
                                count=1
                        for num in num_list:
                                num_string +=str(num)
                        if(count==0):
                                number1=int(num_string)
                                print(number1)
                        if(count==1):
                                number2=int(num_string)
                                print(number2)
                        num_string=""
                        if(box_num=="="):
                                print("it passed")
                                answer=obj1.to_do(number1,number2,operation)
                                print(answer)
                        
                obj1.text()
        pygame.display.flip()
