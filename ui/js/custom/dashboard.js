$(function () {
    // Json data by API call for the order table
    $.get(orderListApiUrl, function (response) {
        if (response) {
            var table = '';
            var totalCost = 0;

            $.each(response, function(index, order) {
                totalCost += parseFloat(order.total);
                table += '<tr>' 
                    +'<td>'+ order.total +' Rs</td>'+
                    '<td>'+ order.order_id  +'</td>'+
                    '<td>'+order.customer_name +'</td>'+ // Assuming datetime is the date property
                    '<td>'+ order.datetime  +'</td>'+'</tr>'; // Assuming total is the price property
            });
            
            table += '<tr><td colspan="3" style="text-align: end"><b>Total</b></td><td><b>'+totalCost +' Rs</b></td></tr>';

            // Clear and update the table body
            $("table").find('tbody').empty().html(table);
        }
    });
});
