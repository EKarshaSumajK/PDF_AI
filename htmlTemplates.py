css = '''
<style>

.chat-message {
    padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 1rem; display: flex
}
.chat-message.user {
    background-color: #2b313e
}
.chat-message.bot {
    background-color: #475063
}
.chat-message .avatar {
  width: 20%;
}
.chat-message .avatar img {
  max-width: 78px;
  max-height: 78px;
  border-radius: 50%;
  object-fit: cover;
}
.chat-message .message {
  width: 80%;
  padding: 0 1.5rem;
  color: #fff;
}
.middle-align {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
        }'''
heading_template='''
<div style="text-align: center;">
    <h1>Chat with PDF</h1>
</div>
'''
bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://static.vecteezy.com/system/resources/thumbnails/010/044/383/small/chat-bot-icon-isolated-contour-symbol-illustration-vector.jpg" style="max-height: 78px; max-width: 78px; border-radius: 50%; object-fit: cover;">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://cdn.pixabay.com/photo/2020/07/01/12/58/icon-5359553_640.png">
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''
instruction_template='''

'''
