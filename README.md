



## 🪨 Rock  Paper Scissors — Modular Python Game

A modular command-line implementation of the classic **Rock–Paper–Scissors** game built in Python — with clean structure and **plans to support multiplayer over local network using sockets**
## 🚀 Features 
- 🎮 Play against another human or the computer 
- 👨‍💻 Modular code — each function lives in its own file for easy maintenance and scalability 
- 📋 Input validation and clear error handling
- ✅ Follows PEP 8 (pycodestyle) and PEP 257 standards 
- 🔌 Future support for **local network multiplayer using sockets** 
## 📁 Project Structure

``` graphql
rock-paper-scissors-socket/  
├── main.py # Entry point of the game  
├── get_user_choice.py # Handles user input (rock/paper/scissors)  
├── get_computer_choice.py # Random choice logic for computer player  
├── get_winner.py # Winner logic based on player choices  
├── get_game_opponent.py # Asks if the user wants single or multiplayer  
├── README.md # You’re here!
```

```yaml

## ▶️ How to Run  
### Prerequisites 
- Python 3.6 or newer  

- ### Run the Game 
```

```bash
python main.py
```

Follow the on-screen prompts to select singleplayer or multiplayer mode and play the game.

---

## 🕹️ Game Modes

1. **Singleplayer** – Play against the computer (AI chooses randomly).
    
2. **Multiplayer (Local)** – Two players take turns on the same machine.
    

> 🛠️ **Coming Soon**: Multiplayer over LAN using Python sockets.

---


## 💡 Example Output

```markdown

_________________________________________________________ 
Rock Paper Scissors Game 
_________________________________________________________  

Select game player type:   
	1. Singleplayer  
	2. Multiplayer  
	
	Selected: 1 
	
_________________________________________________________ 
Player 1: 
_________________________________________________________ 
Pick one:   
	1. Rock  
	2. Paper  
	3. Scissors 
Your choice: 1 
	
Player 1 picked rock while System Player picked scissors. 

Congratulations, you win!
_________________________________________________________
```


## 🧑‍💻 Contributing

Contributions and ideas are welcome! Please open an issue or submit a pull request.

---

## 📜 License

This project is open-source and available under the MIT License.

---

### 👤 Author

Roy Kipchumba

GitHub: @bluebird3624

Email: koechroy06@gmail.com