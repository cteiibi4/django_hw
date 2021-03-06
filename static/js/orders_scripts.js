"use strict";

window.onload = function () {
    let _quantity, _price, orderitemNum, deltaQuantity, orderitemQuantity, deltaCost;
    let quantityArr = [];
    let priceArr = [];
    let $orderTotalQuantityDOM = $('.order_total_quantity');

    // $('.order_total_quantity')
    // document.querySelector('.order_total_quantity').

    let totalForms = parseInt($('input[name="orderitems-TOTAL_FORMS"]').val());
    let orderTotalQuantity = parseInt($orderTotalQuantityDOM.text()) || 0;
    let orderTotalCost = parseFloat($('.order_total_cost').text().replace(',', '.')) || 0;
    let $orderForm = $('.order_form');

    for (let i = 0; i < totalForms; i++) {
        _quantity = parseInt($('input[name="orderitems-' + i + '-quantity"]').val());
        _price = parseFloat($('.orderitems-' + i + '-price').text().replace(',', '.'));
        quantityArr[i] = _quantity;
        priceArr[i] = (_price) ? _price : 0;
    }

    function orderSummaryUpdate(orderitemPrice, deltaQuantity) {
        deltaCost = orderitemPrice * deltaQuantity;
        orderTotalCost = Number((orderTotalCost + deltaCost).toFixed(2));
        orderTotalQuantity = orderTotalQuantity + deltaQuantity;

        $('.order_total_cost').html(orderTotalCost.toString());
        $orderTotalQuantityDOM.html(orderTotalQuantity.toString());
    }

    function deleteOrderItem(row) {
        let targetName = row[0].querySelector('input[type="number"]').name;
        orderitemNum = parseInt(targetName.replace('orderitems-', '').replace('-quantity', ''));
        deltaQuantity = -quantityArr[orderitemNum];
        orderSummaryUpdate(priceArr[orderitemNum], deltaQuantity);
    }

    if (!orderTotalQuantity) {
        for (let i = 0; i < totalForms; i++) {
            orderTotalQuantity += quantityArr[i];
            orderTotalCost += quantityArr[i] * priceArr[i];
        }
        $orderTotalQuantityDOM.html(orderTotalQuantity.toString());
        $('.order_total_cost').html(Number(orderTotalCost.toFixed(2)).toString());
    }

    $orderForm.on('change', 'input[type="number"]', function (event) {
        orderitemNum = parseInt(event.target.name.replace('orderitems-', '').replace('-quantity', ''));
        if (priceArr[orderitemNum]) {
            orderitemQuantity = parseInt(event.target.value);
            deltaQuantity = orderitemQuantity - quantityArr[orderitemNum];
            quantityArr[orderitemNum] = orderitemQuantity;
            orderSummaryUpdate(priceArr[orderitemNum], deltaQuantity);
        }
    });

    $orderForm.on('change', 'input[type="checkbox"]', function (event) {
        orderitemNum = parseInt(event.target.name.replace('orderitems-', '').replace('-DELETE', ''));
        if (event.target.checked) {
            deltaQuantity = -quantityArr[orderitemNum];
        } else {
            deltaQuantity = quantityArr[orderitemNum];
        }
        orderSummaryUpdate(priceArr[orderitemNum], deltaQuantity);
    });

    $('.formset_row').formset({
        addText: 'добавить продукт',
        deleteText: 'удалить',
        prefix: 'orderitems',
        removed: deleteOrderItem
    });

     $orderForm.on('change', 'select', function (event) {
         let target = event.target;
         console.log(target);
     });

};