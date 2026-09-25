(function () {
    const select_variacao = document.getElementById('select-variacoes');
    const variation_preco = document.getElementById('variation-preco');
    const variation_preco_promocional = document.getElementById(
        'variation-preco-promocional'
    );

    if (!select_variacao || !variation_preco || !variation_preco_promocional) {
        return;
    }

    select_variacao.addEventListener('change', function () {
        const preco = this.options[this.selectedIndex]
            .getAttribute('data-preco');

        const preco_promocional = this.options[this.selectedIndex]
            .getAttribute('data-preco-promocional');
            
        console.log('Preço:', preco);
        console.log('Promoção:', preco_promocional);
        
        if (preco_promocional) {
            variation_preco.innerHTML = preco;
            variation_preco_promocional.innerHTML = preco_promocional;

            variation_preco.classList.add('product-old-price', 'text-muted');
            variation_preco.classList.remove('product-price');

            variation_preco_promocional.classList.add('product-price');
            variation_preco_promocional.classList.remove(
                'product-old-price',
                'text-muted'
            );

            variation_preco_promocional.hidden = false;
        } else {
            variation_preco.innerHTML = preco;

            variation_preco.classList.add('product-price');
            variation_preco.classList.remove('product-old-price', 'text-muted');

            variation_preco_promocional.hidden = true;
        }
    });
})();