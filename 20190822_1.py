

def create_model(filename, skip_gram=False):
    tokens = pd.read_csv(filename)
    #tokens = tokens[tokens["contents"].apply(lambda x: 'http' not in x)]

    sentence = tokens["token"].apply(lambda x: ast.literal_eval(x)).tolist()

#skip gram 방법
    model = Word2Vec(sentence, min_count=10, iter=20, size=300, sg=1)

    model.init_sims(replace=True)
    model.save("./result/embedding.model")


    ################3
    import gensim
    model = gensim.models.Word2Vec.load('C:/Users/HYERIN/Downloads/ko/ko.bin')
    print(type(model))
    a = model.wv.most_similar("디자인")
    print(a)
    print(model.similarity('디자인', '인테리어'))


##


