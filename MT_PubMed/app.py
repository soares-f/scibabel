from flask import Flask
from flask import render_template
from flask import request
app = Flask(__name__)

vocabulary = [[('mammary tumors','tumeurs mmammaires'), ('estrogen receptors','Récepteur des œstrogènes'), ('breast cancers','cancers du sein')], [],[],[],[],[],[],[]]

text_tgt = [ "Il existe un besoin désespéré sur le terrain de tumeurs mammaires et de lignées cellulaires de souris qui imitent fidèlement l'expression et l'activité des récepteurs aux œstrogènes (ER) que l'on trouve dans les cancers du sein humain.",

"Nous avons constaté que plusieurs lignées cellulaires de cancer mammaire de souris expriment l'ER mais ne parviennent pas à démontrer une prolifération ou une activité transcriptionnelle induite par les œstrogènes classiques.",

"Nous avons étudié si ces lignées cellulaires peuvent être utilisées pour modéliser la résistance au tamoxifène en utilisant des inhibiteurs de petites molécules pour des voies de signalisation connues pour contribuer à la résistance.",

"Nous avons constaté que la combinaison de l'inhibition de NFκB et des antagonistes ER réduisait de manière significative la prolifération cellulaire in vitro, ainsi que la croissance des tumeurs syngéniques.",

"Étonnamment, nous avons constaté que l'ER était localisée dans le cytoplasme, quel que soit le type de traitement.",

"Sur cette base, nous avons sondé les fonctions extra-nucléaires de l'ER et constaté que la co-inhibition de l'ER et du NFκB entraînait une augmentation du stress oxydatif et de l'apoptose.",

"Ensemble, ces résultats suggèrent que l'ER cytoplasmique et le NFκB peuvent jouer un rôle redondant dans la protection des cellules cancéreuses mammaires contre le stress oxydatif et la mort cellulaire.",

"Bien que cette étude n'ait pas identifié de modèle de souris avec une activité ER classique, l'ER cytoplasmique a été décrite dans un petit sous-ensemble de tumeurs du sein humain, suggérant que ces résultats pourraient être pertinents pour certaines patientes atteintes d'un cancer du sein."
]

text_src = ["There is a desperate need in the field for mouse mammary tumors and cell lines that faithfully mimic estrogen receptor (ER) expression and activity found in human breast cancers.",

"We found that several mouse mammary cancer cell lines express ER but fail to demonstrate classical estrogen-driven proliferation or transcriptional activity.",

"We investigated whether these cell lines may be used to model tamoxifen resistance by using small molecule inhibitors to signaling pathways known to contribute to resistance.",

"We found that the combination of NFκB inhibition and ER antagonists significantly reduced cell proliferation in vitro, as well as growth of syngeneic tumors.",

"Surprisingly, we found that ER was localized to the cytoplasm, regardless of any type of treatment.",

"Based on this, we probed extra-nuclear functions of ER and found that co-inhibition of ER and NFκB led to an increase in oxidative stress and apoptosis.",

"Together, these findings suggest that cytoplasmic ER and NFκB may play redundant roles in protecting mammary cancer cells from oxidative stress and cell death.",

"Although this study has not identified a mouse model with classical ER activity, cytoplasmic ER has been described in a small subset of human breast tumors, suggesting that these findings may be relevant for some breast cancer patients."]


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/parallel')
def show_parallel():
    #print('a')
    #print(text_tgt)
    return render_template('translation_checker.html', text_tgt=text_tgt, text_src=text_src)

@app.route('/parallel_edit')
def edit_parallel():
    #print('a')
    #print(text_tgt)
    return render_template('translation_editor.html', parallel_texts=zip(text_tgt, text_src, vocabulary))

@app.route('/save_edit', methods = ['POST'])
def save_edit():
    if request.method == 'POST':
        """modify/update the information for <user_id>"""
        # you can use <user_id>, which is a str but could
        # changed to be int or whatever you want, along
        # with your lxml knowledge to make the required
        # changes
        data = request.form # a multidict containing POST data

    return render_template('translation_checker.html', text_tgt=text_tgt, text_src=text_src)


if __name__ == '__main__':
    app.run()
