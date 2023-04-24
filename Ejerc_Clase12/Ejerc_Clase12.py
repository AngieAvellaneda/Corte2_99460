
class Ciudadano:
    def __init__(self):
        self.nombre=None
        self.cc=None
        self.educacion=None

#------------Setters----------------
    def setNombre(self,nombre:str):
        self.nombre=nombre
    def setCc(self,cc:int):
        self.cc=cc
    def setEducacion(self,educacion:str):
        self.educacion=educacion

#-----------Getters-----------------
    def getNombre(self):
        return self.nombre
    def getCc(self):
        return self.cc
    def getEducacion(self):
        return self.educacion
    
#-----------Metodo---------------
    def trabajar(self):
        print('Estoy trabajando')

class Ingeniero(Ciudadano):
    def __init__(self):
        super().__init__()
        self.__area=None
        self.__cantProyec=None

#------------Setters----------------
    def setArea(self,area:str):
        self.__area=area
    def setCantProyec(self,cantProyec:int):
        self.__cantProyec=cantProyec

#-----------Getters-----------------
    def getArea(self):
        return self.__area
    def getCantProyec(self):
        return self.__cantProyec
   
#-----------Metodo---------------
    def trabajar(self):
        print(f'Estoy trabajando en el area de: {self.getArea()}')

    #-----------Metodo---------------
    def construir(self):
        print('Estoy construyendo un proyecto')
    
class Cocinero(Ciudadano):
    def __init__(self):
        super().__init__()
        self.__tipoCocina=None
        self.__platoEsp=None

#------------Setters----------------
    def setTipoCocina(self,tipoCocina:str):
        self.__tipoCocina=tipoCocina
    def setPlatoEsp(self,platoEsp:str):
        self.__platoEsp=platoEsp

#-----------Getters-----------------
    def getTipoCocina(self):
        return self.__tipoCocina
    def getPlatoEsp(self):
        return self.__platoEsp
   
#-----------Metodo---------------
    def trabajar(self):
        print(f'Estoy haciendo mi plato especial: {self.getPlatoEsp()}')

    #-----------Metodo---------------
    def cocinar(self):
        print('Estoy cocinando para 100 personas')
  
class Modelo(Ciudadano):
    def __init__(self):
        super().__init__()
        self.__altura=None
        self.__atributo=None
        self.__empresa=None
#------------Setters----------------
    def setAltura(self,altura:float):
        self.__altura=altura
    def setAtributo(self,atributo:str):
        self.__atributo=atributo
    def setEmpresa(self,empresa:str):
        self.__empresa=empresa
#-----------Getters-----------------
    def getAltura(self):
        return self.__altura
    def getAtributo(self):
        return self.__atributo
    def getEmpresa(self):
        return self.__empresa
#-----------Metodo---------------
    def trabajar(self):
        print(f'Estoy modelando para: {self.getEmpresa()}')

    #-----------Metodo---------------
    def modelar(self):
        print('Estoy modelando ropa vintage')
  

def main():
    ciudadano = Ciudadano()
    ciudadano.setNombre('Rafael')
    ciudadano.setCc(5643214567)
    ciudadano.setEducacion('Bachiller')

    ingeniero = Ingeniero()
    ingeniero.setNombre('Angie')
    ingeniero.setCc(1028781117)
    ingeniero.setEducacion('Profesional')
    ingeniero.setArea('Mecatronica')
    ingeniero.setCantProyec(15)

    cocinero = Cocinero()
    cocinero.setNombre('Milena')
    cocinero.setCc(52824370)
    cocinero.setEducacion('Profesional')
    cocinero.setTipoCocina('Gourmet')
    cocinero.setPlatoEsp('Arroz atoyado')

    modelo = Modelo()
    modelo.setNombre('Paola')
    modelo.setCc(1049568723)
    modelo.setEducacion('Profesional')
    modelo.setAltura('1.75')
    modelo.setAtributo('Cabello largo')
    modelo.setEmpresa('Prada')


    print(f'\nHola mi nombre es {ciudadano.getNombre()} y soy {ciudadano.getEducacion()}')
    print('Mi metodo es:')
    ciudadano.trabajar()

    print(f'\nHola mi nombre es {ingeniero.getNombre()} y soy {ingeniero.getEducacion()}')
    print('Mi metodo de sobrecarga es:')
    ingeniero.trabajar()
    print('Mi metodo unico es: ')
    ingeniero.construir()


    print(f'\nHola mi nombre es {cocinero.getNombre()} y soy {cocinero.getEducacion()}')
    print('Mi metodo de sobrecarga es:')
    cocinero.trabajar()
    print('Mi metodo unico es: ')
    cocinero.cocinar()


    print(f'\nHola mi nombre es {modelo.getNombre()} y soy {modelo.getEducacion()}')
    print('Mi metodo de sobrecarga es:')
    modelo.trabajar()
    print('Mi metodo unico es: ')
    modelo.modelar()


if __name__=="__main__":
    main()
