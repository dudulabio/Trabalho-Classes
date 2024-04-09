from fazenda import Fazenda
from defensivos import Defensivos
from pragas import Pragas

#criar uma constante com a informação do dir. de exportação

#criando objeto do tipo Fazenda, chamado faz1
faz1 = Fazenda(nome="Fazenda Ouro Verde", area=3000, proprietario="Paulin")

## self, produto, mecanismo, titular, formulacao, toxicidade, ambientacao)

defensivo1 = Defensivos("Acefato Fersol 750 SP", "acefato", "Ameribrás Indústria e Comércio Ltda", "SP - Pó Solúvel",4,"III")
defensivo2 = Defensivos("Aplaud 250","bupprofezina","Nichino do Brasil Agroquimicos Ltda", "WP - Pó Molhável", 5, "III")
defensivo3 = Defensivos("Closer SC","sulfoxaflor","CTVA Proteção de Cultivos Ltda", "SC - Suspensão Concentrada", "Não", "III")
defensivo4 = Defensivos("Dinky 200 SP","acetamiprido","Globachem Proteção de Cultivos do Brasil Ltda.", "SP - Pó Solúvel",4, "II")


faz1.addDefensivosLista(defensivo1)
faz1.addDefensivosLista(defensivo2)
faz1.addDefensivosLista(defensivo3)
faz1.addDefensivosLista(defensivo4)

faz1.imprimirListaDefensivos()






## self,classificacao, nome_cientifico, cultura, nome_vulgar, ordem, familia, sintomas, bioecologia, controle, mecanismo
praga1 = Pragas("Inseto", "Dichelops Furcatus", "Soja", "Percevejo Barriga Verde", "Hemiptera/Heteroptera", "Pentatomidae", "Os prejuízos causados resultam da saliva deixada pelos insetos durante o processo de sucção de seiva nos ramos e hastes, fator que é limitante para a produção. Também provocam a retenção foliar.", "São insetos de coloração marrom e comprimento de 9 mm. A oviposição acontece sobre a folhagem das plantas hospedeiras. O seu ciclo completa-se em aproximadamente 45 dias.","CONTROLE QUÍMICO: Fazer uso de inseticidas específicos", "Alfa-cipermetrina+dinotefuram+isocicoseram+lambda-cialotrina")

praga2 = Pragas("Inseto", "Euschistus heros", "Soja", "Percevejo Marrom","Hemiptera/Heteroptera", "Pentatomidae", "Estes insetos danificam as vagens e os grãos, além de provocarem uma retenção foliar, dificultando o processo da colheita mecânica.", "O inseto adulto apresenta coloração marrom uniforme. O protórax tem dois espinhos laterais e no ápice do escutelo observa-se uma mancha branca em forma de meia lua.A oviposição ocorre nas vagens ou nas folhas. Os ovos apresentam coloração amarela. As ninfas são marrom-amareladas, tornando-se esverdeadas com a mudança dos ínstares. O ciclo biológico dessa praga dura aproximadamente 40 dias.", "CONTROLE QUÍMICO: Fazer uso de inseticidas específicos", "Acefato + Azoxistrobina + Acetamiprido + Clorpirifoz + cipermetrina + bifentrina + malationa + acetamiprido + azadiractina + beta-ciflutrina")

praga3 = Pragas("Inseto", "Bemisia Tabaci", "Soja", "Mosca Branca", "Hemiptera/Heteroptera", "Aleyrodidae","Estes insetos, adultos ou ninfas, causam perdas significativas nas culturas, seja pela queda das folhas e frutos, murchamento, além do amadurecimento irregular dos frutos.Causam ainda sérios problemas devido à infecção de vírus, que provoca paralisação do crescimento e queda na produção, quando não leva a planta à morte.", "Os adultos têm o branco como cor predominante, uma vez que suas asas cobrem a maior parte de corpo e possuem essa coloração, no entanto o dorso é amarelo-claro. Quanto ao tamanho, pode-se dizer ainda que os machos são menores que as fêmeas. O aparelho bucal é do tipo picador-sugador.A oviposição ocorre de maneira isolada na parte inferior da folha. Os ovos apresentam o formato de uma pêra, além da coloração amarelada. Após a eclosão, surgem as ninfas, essas são translúcidas e de coloração que pode variar do amarelo ao amarelo-pálido. Logo no início de seu desenvolvimento, saem à procura de um local na planta para que possam introduzir o estilete e começar o processo de sucção de seiva. Após o primeiro estádio, as ninfas permanecem imóveis até a fase de pupa, apenas se alimentando. A longevidade da fêmea é de aproximadamente 18 dias" ,"Utilizar sementes de boa qualidade, além das variedades mais resistentes + CONTROLE QUÍMICO: Fazer uso de inseticidas específicos","Acefato + buprofezina + sulfoxaflor+ acetamiprido + lambda-cialotrina")

praga4 = Pragas("Inseto", "Empoasca Kraemeri", "Soja", "Cigarrinha Verde","Hemiptera/Homoptera", "Cicadelidae", "Tanto as ninfas quanto os adultos encontram-se na parte inferior das folhas sugando a seiva. Os sintomas dessa praga são muito semelhantes à ocorrência de viroses. Os danos na planta são causados devido às toxinas que são inoculadas na planta durante a alimentação do inseto.Quando o ataque é muito intenso observa-se o enfezamento das plantas, tendo como característica os folíolos enrolados para baixo, e, quando esse ataque fica mais severo, a borda dos folíolos apresenta uma coloração amarelada, acompanhada de secamento", "Os insetos adultos medem 3 mm de comprimento e possuem coloração verde.A oviposição é preferencialmente realizada ao longo das nervuras das folhagens, sendo que a média é de 60 ovos para cada fêmea. A locomoção das ninfas geralmente é de forma lateral; essas possuem coloração verde-clara e, assim como os adultos, são ágeis. Para que o ciclo se complete normalmente são necessários em torno de 21 dias.", "CONTROLE QUÍMICO: Fazer uso de inseticidas específicos", "Acefato")


faz1.addPragasLista(praga1)
faz1.addPragasLista(praga2)
faz1.addPragasLista(praga3)
faz1.addPragasLista(praga4)

faz1.imprimirListaPragas()
