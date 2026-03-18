🎮 Simulação de Texto Quicando (Pygame)

Este projeto foi desenvolvido em Python utilizando a biblioteca Pygame.
A ideia é criar uma animação simples onde dois textos se movimentam pela tela e reagem quando encostam nas bordas ou um no outro.

O comportamento lembra aquele efeito clássico do logo do DVD quicando na tela.

🛠 Tecnologias utilizadas

Python 3

Biblioteca Pygame

📌 Como o programa funciona

O programa abre uma janela com resolução 800x600 pixels.
Dentro dessa janela, dois textos se movimentam continuamente em direções aleatórias.

Durante a execução do programa acontecem alguns eventos:

Cada texto começa com velocidade aleatória

Quando um texto encosta na borda da tela, ele muda de direção

Quando os dois textos colidem entre si, eles trocam suas velocidades

Sempre que ocorre uma colisão, a cor do texto muda aleatoriamente

Isso cria uma pequena animação dinâmica.

🧩 Organização do código

Para deixar o código mais organizado, algumas partes foram separadas em funções específicas.

gerar_velocidade()

Essa função gera valores aleatórios para a velocidade horizontal (vx) e vertical (vy).

Ela garante que o valor não seja (0,0), pois isso faria o objeto ficar parado.

def gerar_velocidade():
    while True:
        vx = random.randint(-1, 1)
        vy = random.randint(-1, 1)
        if vx != 0 or vy != 0:
            return vx, vy
cor_aleatoria()

Cria uma cor RGB aleatória.

def cor_aleatoria():
    return (
        random.randint(1, 255),
        random.randint(1, 255),
        random.randint(1, 255),
    )

Essa função é utilizada sempre que ocorre algum tipo de colisão.

criar_texto()

Responsável por criar o objeto de texto que será exibido na tela.

Ela:

Renderiza o texto usando a fonte escolhida

Cria o retângulo de colisão (rect)

Define a posição inicial

def criar_texto(fonte, texto_str, cor, posicao):
    texto = fonte.render(texto_str, True, cor)
    rect = texto.get_rect(center=posicao)
    return texto, rect
atualizar_colisao_borda()

Essa função verifica se o texto atingiu alguma borda da tela.

Caso isso aconteça:

A direção do movimento é alterada

O texto recebe uma nova cor

def atualizar_colisao_borda(rect, vx, vy, fonte, texto_str):

Ela retorna a nova velocidade e, se necessário, o texto atualizado.

main()

Essa é a função principal do programa.

Nela acontece:

Inicialização do Pygame

Criação da janela

Criação dos textos

Execução do loop principal

Atualização do movimento

Verificação de colisões

Renderização dos elementos na tela

O loop principal continua rodando até o usuário fechar a janela.

💥 Colisão entre os textos

A colisão entre os dois textos é detectada com:

rect1.colliderect(rect2)

Quando ocorre o contato:

As velocidades dos textos são trocadas

Ambos recebem novas cores aleatórias

Isso cria um efeito simples de impacto entre os objetos.

▶ Execução do projeto

Para executar o projeto:

Instale o Pygame

pip install pygame

Execute o arquivo Python

python main.py

Uma janela será aberta mostrando a animação dos textos se movimentando pela tela.