from openai import OpenAI

class WizardSData:
    def __init__(self, **kwargs):
        self.roles_dataset = kwargs.get('roles_dataset')
        self.topics_dataset = kwargs.get('topics_dataset')
        self.api_key = kwargs.get('api_key')
        self.num_questions = kwargs.get('num_questions', 10)
        self.num_questions_per_topic = kwargs.get('num_questions_per_topic', 3)

        self._validate_inputs()

    def _validate_inputs(self):
        if not self.roles_dataset or not self.topics_dataset:
            raise ValueError("Both 'roles_dataset' and 'topics_dataset' are required.")
        if not self.api_key:
            raise ValueError("OpenAI API key is required.")

    def generate_dataset(self):
        # Configuración de la API
        OpenAI.api_key = self.api_key

        # Lógica simplificada para generar dataset (ejemplo base)
        dataset = []
        for role in self.roles_dataset:
            for topic in self.topics_dataset:
                for _ in range(self.num_questions_per_topic):
                    prompt = f"{role} asks about {topic}:"
                    response = self._query_openai(prompt)
                    dataset.append({
                        "role": role,
                        "topic": topic,
                        "question": prompt,
                        "response": response
                    })
        return dataset

    def _query_openai(self, prompt):
        # Llamada simple a la API (puedes ajustar según el modelo que uses)
        response = OpenAI.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=100
        )
        return response.choices[0].text.strip()
