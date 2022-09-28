from transformers import pipeline
from tmh.text.translate import translate_between_languages

def generate_text(model='EleutherAI/gpt-neo-2.7B', prompt="chatbot", max_length=200, temperature=0.9):
    generator = pipeline('text-generation', model=model)
    output = generator(prompt, do_sample=True, temperature=temperature, max_length=max_length)
    return output[0]['generated_text']

prompt = ''' This is a discussion between a [human] and a [robot]. 
The [robot] is very nice and empathetic.

[human]: Hello nice to meet you.
[robot]: Nice to meet you too.
###
[human]: How is it going today?
[robot]: Not so bad, thank you! How about you?
###
[human]: I am ok, but I am a bit sad...
[robot]: Oh? Why that?
###
[human]: I broke up with my girlfriend...
[robot]: 
                    '''

output = generate_text(model='EleutherAI/gpt-neo-2.7B', prompt="EleutherAI has", min_length=150)
print(output)