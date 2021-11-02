'''
o nome do arquivo 'modelo' foi escolhido
por que normalmente quando se cria um arquivo
em projetos de POO se da esse nome ao arquivo
que dara o conceito de classes que teram/daram
um dominio no nosso sistema.
'modelar uma classe é contruir ela, dar vida.'
'''
'''
Sempre tentar diminuir a complexidade do programa,
quando eu coloquei a plasse playlist para herdar da superclasse list 
eu perdi o uso para varias das funçoes que eu ja tinha escrito
por conta de uma unica facilidade besta que acabou gerando uma complexidade
enorme pra eu poder reescrever os mesmos metodos depois,
logo tem que ficar ligado nisso, quanto menos complexidade melhor.
'''
################ Classes #######################################
class Programa: #'Programa' de Programa de televisao =).
    def __init__(self, nome , ano , likes = 0):
        self._nome = nome
        self._ano = ano
        self._likes = likes
        '''note que aqui usei so um underscore anted dos atributos
        isso define que esses atributos estao 'protegidos' oq em 
        java seria o protected, logo os atributos podem ser utilizados 
        pelas subclasses da classe Programa mas nao por outras classes,
        so se pedir permissao.
        '''
    #os get
    @property
    def nome(self):
        self._nome = str(self._nome).title()
        return self._nome
    @property
    def ano(self):
        return self._ano
    @property
    def likes(self):
        return int(self._likes)
    #os set
    @nome.setter
    def nome(self,novo_nome):
        self._nome = str(novo_nome).title()
    @ano.setter
    def ano(self,novo_ano):
        self._ano = novo_ano
    @likes.setter
    def likes(self,valor):
        self._likes = int(self._likes) + int(valor)

    #metodos da classe
    def dar_like(self):
        self._likes = self._likes + 1
    '''
    def imprime(self):
        return print(f'nome: {self._nome} - ano: {self._ano} - likes: {self._likes}')
    '''
    # agora vou utilizar um codigo str especial que vai fazer a mesma funçao que esse metodo imprime,
    # a unica diferença é que fica mais bonito e utiliza uma funçao bult-in tornando o codigo mais 'PYTONICO'.
    def __str__(self):
        return f'nome: {self._nome} - ano: {self._ano} - likes: {self._likes}'
    # note que o __str__ returna uma string e só uma string, entao tem que mandar ele retornar uma string se nao da erro, bro.
class Filme(Programa):
    def __init__(self, nome , ano , duracao, likes=0):
        super().__init__(nome, ano , likes)#chama os atributos que ja foram definidos na classe mae, ou super classe.
        self.__duracao = duracao
    @property
    def duracao(self):
        return self.__duracao
    @duracao.setter
    def duracao(self,nova_duracao):
        self.__duracao = nova_duracao

    #metodos da classe
    '''
    def imprime(self):
        return print(f'nome: {self._nome} - ano: {self._ano} - duração: {self.__duracao} - likes: {self._likes}')
    '''
    def __str__(self):
        return f'nome: {self._nome} - ano: {self._ano} - duração: {self.__duracao} - likes: {self._likes}'
    #(basicamente um ToString() de java)
class Serie(Programa):
    def __init__(self, nome, ano, temporadas, likes=0):
        super().__init__(nome , ano , likes)
        self.__temporadas = temporadas
    @property
    def temporadas(self):
        return self.__temporadas
    @temporadas.setter
    def temporadas(self,valor):
        self.__temporadas = valor

    #metodos da classe
    '''
    def imprime(self):
        return print(f'nome: {self._nome} - ano: {self._ano} - temporadas: {self.__temporadas} - likes: {self._likes}')
    '''
    def __str__(self):
        return f'nome: {self._nome} - ano: {self._ano} - temporadas: {self.__temporadas} - likes: {self._likes}'
    #(basicamente um ToString() de java)
class Playlist(Programa):
    def __init__(self, nome_da_playlist, programas_na_playlist):
        self.__nome_da_playlist = nome_da_playlist
        self.__programas_na_playslist = programas_na_playlist
    #gets e sets
    @property
    def nome_da_playlist(self):
        return str(self.__nome_da_playlist).title()
    @nome_da_playlist.setter
    def nome_da_playlist(self,valor):
        self.__nome_da_playlist = valor
    @property
    def programas_na_playlist(self):
        return self.__programas_na_playslist

    def __str__(self):
        return f'Playlist de nome: {self.nome_da_playlist}; Tamanho: {self.tamanho}; Lista de nomes: {self.reprensentaçao_nome_dos_objetos_da_playlist()};'

    ##inicio
    '''Se eu quero que o objeto Paylist se comporte como um iteravel 
    eu devo utilizar uma artimanha chamada 'duck tiping', que vem do ditado
    "se anda como um pato, voa como um pato e faz quack. entao deve ser um pato",
    ou seja, se eu quero que o meu objeto se comporte como um iteravel eu devo colocar
    metodos que adicione tais comportamentos ao mesmo. É oq vamos fazer quando implementarmos
    o metodo '__getitem__' no codigo, pois esse metodo é um metodo que esta por debaixo dos 
    panos em qualquer objeto iteravel do Python, logo, nosso objeto Playlist tendo os metodos
    de iteraveis e tbm agindo como um iteravel o Python vai la e pensa 'ora, esse objeto deve
    ser um iteravel tbm ' iguala o ditado.'''
    def __getitem__(self, item):
        return self.programas_na_playlist[item]
    '''Aqui colocamos o metodo especial, muitas vezes tambem chamado de magico(magic method)
    ou ate mesmo 'DANDER method' 
    para retornar a lista que queremos iteragir com, pois o objeto iteravel deve ser iteragivel
    com algo, entao nos vamos la e dizemos com oq o metodo deve ser itegarivel quando solicitarmos
    tal ação la no __main__, dai temos que , quanod solicitado, o objeto deve atraves desse metodo
    tornar iteravel cada item dentro da lista privada '__programas_na_playlista' que iremos integarir 
    atraves da '@property' do atributo.'''
    ##fim

    ##inico
    '''Para fazer com que o meu objeto tenha uma iterabilidade com o metodo len(), 
    nao sendo ele uma lista(pq fizemos um ducktiping utilizando um dander method para que minhas
    playlists se tornassem iteraveis como uma lista), teremos que implementar um novo dander method
    ou magic method chamado '__len__' que vai fazer com que minha playlist tenha iterabilidade com 
    o meu metodo len().
    '''
    def __len__(self):
        return len(self.__programas_na_playslist)
    '''dessa forma quanod o len() for chamado fora do objeto, ele vai returnar o resultado 
    do metodo len() sobre a lista playlista que é uma variavel interna e por isso o 
    metodo len() funciona dentro do objeto, e agora ele tambem ira funcionar fora do objeto '''
    ##fim

    #metodos da classe
    #depois da herança em list eu nao preçido mais de uma funçao pois eu posso usar o len() direto no objeto
    @property
    def tamanho(self):
        return len(self.__programas_na_playslist)

    def retorna_lista_de_objetos_da_playlist(self):
        return self.__programas_na_playslist

    '''Esse metodo 'retorna_lista_representada_em_string()' se torna 
    obsoleto depois da implementaçao do __getitem__ mas vou deixar aqui
    disponivel para fins de estudo de caso.'''
    def retorna_lista_representada_em_string(self):
        print(f"\n>Lista do Objeto tipo Playlist de nome({self.nome_da_playlist}) sendo representada em String<")
        for p in self.programas_na_playlist:
            print(p)
        print(">Fim da representaçao<\n")
    ##

    def reprensentaçao_nome_dos_objetos_da_playlist(self):
        lista =[]
        for p in self.programas_na_playlist:
            lista.append(str(p.nome))
        return lista



############### MAIN ###########################################
if(__name__ == "__main__"):
    #1
    # declaro meus objetos
    vingadores = Filme("vingadores: guerra infinita", 2018, 160, 98)
    atlanta = Serie("atlanta", 2017, 2, 8)
    '''
    vingadores = Filme("vingadores: guerra infinita",2018,160)
    print("-"*30+"\n"+f'Filme: {vingadores.nome}\nAno: {vingadores.ano}\nDuraçao: {vingadores.duracao}\nLikes: {vingadores.likes}\n'+"-"*30)
    vingadores.dar_like()
    #atlanta = Serie("atlanta",2017,2,8)
    #print("-" * 30 + "\n" + f'Serie: {atlanta.nome}\nAno: {atlanta.ano}\nTemporadas: {atlanta.temporadas}\nLikes: {atlanta.likes}\n' + "-" * 30)
    print("-"*30+"\n"+f'Filme: {vingadores.nome}\nAno: {vingadores.ano}\nDuraçao: {vingadores.duracao}\nLikes: {vingadores.likes}\n'+"-"*30)
    '''

    #2
    #vamos criar uma lista que vai receber os objetos
    filmes_e_series = [vingadores , atlanta]
    '''
    #fariamos assim se nao tivessemos o metodo polimorfo 'imprime' nas classes... vou deixar aqui so como exemplo de como utilizar o metodo 'hasattr()'.
    for programas in filmes_e_series:
        detalhes = programas.duracao if hasattr(programas,"duracao") else programas.temporadas
        print(f" {programas.nome} - {detalhes} - {programas.likes}")
    '''
    '''
    for programas in filmes_e_series:
        #programas.imprime()
        #agora deposi de utilizar o __str__ eu posso fazer, simplismente:
        print(programas)
        #e a funçao __str__ vai ser chamada automaticamente quando eu quiser 'imprimir' meu objeto(basicamente um ToString() de java)
    '''

    #3
    #vou delcarar mais obe=jetos para popular minha playlist
    todo_mundo_em_panico = Filme("todo mundo em panico",2003,96,347)
    demolidor = Serie('demolidor: o homen sem medo', 2016 , 2 , 978)

    #vou inserir os objetos na lista filems_e_series
    filmes_e_series.append(todo_mundo_em_panico)
    filmes_e_series.append(demolidor)

    #vou criar minha playlist
    playlist_de_fim_de_semana = Playlist("fim de semana",filmes_e_series)
    print(playlist_de_fim_de_semana)

    #possivel com a implementaçao do __getitem__
    ##inicio
    print(demolidor in playlist_de_fim_de_semana)

    for p in playlist_de_fim_de_semana:
        print(p)
    print(f'tamanho da lista usando metodo interno do objeto tamanho = {playlist_de_fim_de_semana.tamanho}')
    print(f'tamanho da lista usando metodo len() = {len(playlist_de_fim_de_semana)}')
    ##fim

    #playlist_de_fim_de_semana.retorna_lista_representada_em_string()



