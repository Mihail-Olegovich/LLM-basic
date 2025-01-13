# ML System Design Interview Assistant

## Описание проекта
Интерактивный ассистент для подготовки к собеседованиям по ML System Design.
![screen](images/image.png)

## Основные возможности
- Загрузка и обработка PDF документов с материалами по ML System Design
- Создание векторного хранилища на основе документов с использованием FAISS
- Интерактивный чат-интерфейс на базе Gradio
- Генерация ответов с использованием GigaChat и RAG

## Технологический стек
- Python 3.9+
- LangChain для работы с LLM и RAG
- GigaChat в качестве языковой модели
- FAISS для векторного хранилища
- Sentence Transformers для эмбеддингов (all-mpnet-base-v2)
- Gradio для веб-интерфейса

## Как запустить?

### Локальный запуск

1. Установите зависимости:
```bash
pip install -r requirements.txt
```

2. Создайте файл .env в корневой директории проекта со следующими переменными:
```markdown
GIGACHAT_API_KEY=your_api_key_here
```

3. Запустите приложение:
```bash
python -m src.main
```

### Docker запуск

1. Соберите Docker образ:
```bash
docker build -t ml-system-design-assistant .
```

2. Запустите контейнер:
```bash
docker run -p 7860:7860 ml-system-design-assistant
```

### Доступ к приложению

После запуска приложение будет доступно по адресу: [http://localhost:7860](http://localhost:7860)

### Команда

- [Куляскин Михаил](https://github.com/Mihail-Olegovich)
- [Потехин Александр](https://github.com/alpotekhin)
- [Кандрюков Михаил](https://github.com/kandrewkov)
