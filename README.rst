==========================
Trinket templating: Jinja2
==========================

*******
Example
*******

.. code-block:: python
    
    from trinket import Trinket, Response
    from trinket_jinja2 import jinja2
    from pathlib import Path
    
    bauble = jinja2(Trinket(), cache='/tmp/trinket_examples')
    
    @bauble.route('/page')
    async def page_with_jinja2_template(request):
        template = bauble['jinja2'].template(
            Path(__file__).parent / Path('tests/test.jinja2'))
        html = await template(title='Curio HTTP Server', name='Trinket')
        return Response.html(html)
    
    bauble.start()
