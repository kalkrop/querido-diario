from datetime import date

from gazette.items import Gazette
from gazette.spiders.base import BaseGazetteSpider


class UFMunicipioSpider(BaseGazetteSpider):
    name = "to_tupirama"
    TERRITORY_ID = ""
    allowed_domains = ["www.tupirama.to.gov.br"]
    start_urls = ["https://www.tupirama.to.gov.br/diariooficial"]
    start_date = date()

    def parse(self, response):
        # Lógica de extração de metadados

        # partindo de response ...
        #
        # ... o que deve ser feito para coletar DATA DO DIÁRIO?
        # ... o que deve ser feito para coletar NÚMERO DA EDIÇÃO?
        # ... o que deve ser feito para coletar se a EDIÇÃO É EXTRA?
        # ... o que deve ser feito para coletar a URL DE DOWNLOAD do arquivo?

        yield Gazette(
            date=date(),
            edition_number="",
            is_extra_edition=False,
            file_urls=[""],
            power="executive",
        )
