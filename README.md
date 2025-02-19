# Phishing do Desafio do Curso de CiberSecurity Specialist, que possui o objetivo de captura de senhas do Facebook com uma página de login falsa.

# Ferramentas Utilizadas:

**Sistema Operacional:** Kali Linux
**Ferramenta:** setoolkit

------------

## Configurando o Phishing no Kali Linux

1. **Acesso root:**
   ```bash
   sudo su
   > Inserir a senha do usuário
   ```
   - Acesso para obter privilégios de superusuários no Linux, com permissões de comandos administrativos.

2. **Iniciando o setoolkit:**
   ```bash
   setoolkit
   ```
   - Inicia o framework de engenharia social para criarmos o phishing.
 
3. **Selecionando o tipo de ataque:**
   - **Social-Engineering Attacks**: Ataques baseados em engenharia social para explorar vulnerabilidades humanas.
   - **Web Site Attack Vectors**: Métodos para atacar usuários através de sites clonados e técnicas de phishing.

4. **Método de ataque:**
   - **Credential Harvester Attack Method**: Captura credenciais inseridas por usuários em páginas falsas.
   - **Site Cloner**: Clona um site legítimo para enganar usuários e coletar dados.

5. **Obtendo o endereço da máquina:**
   ```bash
   ifconfig
   ```
   - Exibe informações sobre as interfaces de rede, incluindo o endereço IP da máquina para hospedar a página falsa.

6. **URL para clone:**
   ```
   http://www.facebook.com
   ```
   - Define a URL do site que será clonado para enganar usuários e capturar credenciais.

---

## Conclusão

Após a configuração e execução do ataque de phishing, a página clonada do Facebook foi disponibilizada no IP da máquina Kali Linux. Quando um usuário acessa a página e tenta realizar o login, as credenciais de e-mail e senha são capturadas e armazenadas no arquivo de logs do setoolkit. Após isso, o usuário é automaticamente redirecionado para a página principal do Facebook, sem causar nenhuma desconfiança por parte dos usuários.

Os principais resultados observados foram:

- O phishing foi bem-sucedido na simulação, demonstrando a vulnerabilidade de usuários que não verificam a autenticidade do site.
- As credenciais digitadas na página clonada foram registradas em tempo real no terminal do Kali Linux.
- A captura das informações ocorreu de maneira transparente para o usuário, que não percebeu estar interagindo com um site falso.
- Esse teste reforça a importância da conscientização sobre segurança digital e o uso de autenticação multifator para mitigar riscos.

**Observação:** Este teste foi realizado exclusivamente para fins educacionais e de conscientização sobre cibersegurança. A realização de ataques de phishing sem consentimento é ilegal e antiética.

![password](https://github.com/user-attachments/assets/2bb77634-1c57-4aed-94cf-3c0b77f339c6)


