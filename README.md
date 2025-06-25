# Simulação de Ataque DDoS

Este projeto demonstra uma simulação de um ataque DDoS (Distributed Denial of Service).

## 📋 Pré-requisitos

Antes de começar, certifique-se de ter os seguintes componentes instalados:

### 1. Python
- **Versão**: Python 3.7 ou superior
- **Download**: [https://www.python.org/downloads/](https://www.python.org/downloads/)
- **Verificação**: Abra o terminal e digite:
  ```bash
  python --version
  ```

### 2. Pip (Gerenciador de Pacotes Python)
- Geralmente vem junto com o Python
- **Verificação**:
  ```bash
  pip --version
  ```

## 🚀 Configuração do Projeto

### Passo 1: Clone ou Baixe o Projeto
```bash
git clone https://github.com/RicardoMFranca/ddos-simulation
cd ddos-simulation
```

### Passo 2: Instalar Dependências

#### Para o Servidor (Vítima):
```bash
pip install flask
```

#### Para o Atacante:
```bash
pip install requests
```

## 🎯 Como Executar a Simulação

### Cenário: Dois Computadores
Para uma simulação mais realista, use dois computadores diferentes.

---

## 🖥️ Configurando o Servidor (Vítima)

### Passo 1: Identificar o IP do Servidor
1. Abra o terminal no computador que será o servidor
2. Assim que você iniciar o servidor, aparecerá o IP EX: http://192.168.0.102:5000/

### Passo 2: Abrir o servidor
1. Navegue até a pasta do projeto:
   ```bash
   cd ./victim
   ```

2. Execute o servidor:
   ```bash
   python server.py
   ```

### Passo 3: Testar o Servidor
- Abra um navegador no computador servidor
- Acesse: `http://localhost:5000`
- Você deve ver: "Servidor está online!"

---

## ⚔️ Configurando o Atacante

### Passo 1: Configurar o Endereço do Alvo
1. Abra o arquivo `attacker/ddos.py` em um editor de texto
2. Substitua `"ENDEREÇO_DO_SERVIDOR"` pelo IP do servidor:
   ```python
   requests.get("http://192.168.1.100:5000", timeout=1)
   ```
   *(Substitua 192.168.1.100 pelo IP real do seu servidor)*

### Passo 2: Executar o Ataque
1. Navegue até a pasta do atacante:
   ```bash
   cd ddos-simulation/attacker
   ```

2. Execute o script de ataque:
   ```bash
   python ddos.py
   ```

---

## 📊 Monitorando a Simulação

### No Servidor (Vítima):
- Observe se o servidor continua respondendo
- Monitore o uso de CPU e memória
- Verifique se as requisições estão chegando (Recomendamos o WireShark)

### No Atacante:
- O script criará 100 threads simultâneas
- Cada thread fará requisições contínuas ao servidor
- Para parar o ataque, pressione `Ctrl+C`


---

## 🛠️ Solução de Problemas

### Servidor não inicia:
- Verifique se a porta 5000 não está em uso
- Certifique-se de que o Flask está instalado
- Verifique se está no diretório correto

### Ataque não funciona:
- Verifique se o IP do servidor está correto
- Confirme se ambos os computadores estão na mesma rede
- Teste a conectividade com `ping`

### Erro de permissão:
- Execute o terminal como administrador (Windows)
- Use `sudo` no Linux/Mac se necessário


---