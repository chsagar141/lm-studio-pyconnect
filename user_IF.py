import tkinter as tk
from tkinter import scrolledtext
from openAi import OpenAI  # Import the OpenAI module

def get_response():
    user_input = user_entry.get()
    if user_input:
        client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")
        completion = client.chat.completions.create(
            model="model-identifier",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_input}
            ],
            temperature=0.7,
        )
        response = completion.choices[0].message.content
        chat_display.insert(tk.END, "You: " + user_input + "\n", "user")
        chat_display.insert(tk.END, "AI: " + response + "\n\n", "ai")
        user_entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("AI Chat Interface")
root.geometry("500x400")

# Chat display
chat_display = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=15)
chat_display.pack(pady=10)
chat_display.tag_config("user", foreground="blue")
chat_display.tag_config("ai", foreground="green")

# User input field
user_entry = tk.Entry(root, width=50)
user_entry.pack(pady=5)

# Send button
send_button = tk.Button(root, text="Send", command=get_response)
send_button.pack()

# Run the application
root.mainloop()